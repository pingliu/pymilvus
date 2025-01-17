from .constants import OFFSET, LIMIT, ID, FIELDS, RANGE_FILTER, RADIUS, PARAMS, ITERATION_EXTENSION_REDUCE_RATE
from .types import DataType
from ..exceptions import (
    MilvusException,
)


class QueryIterator:

    def __init__(self, connection, collection_name, expr, output_fields=None, partition_names=None, schema=None,
                 timeout=None, **kwargs):
        self._conn = connection
        self._collection_name = collection_name
        self._expr = expr
        self._output_fields = output_fields
        self._partition_names = partition_names
        self._schema = schema
        self._timeout = timeout
        self._kwargs = kwargs
        self.__setup__pk_is_str()
        self.__seek()
        self._cache_id_in_use = NO_CACHE_ID

    def __seek(self):
        self._cache_id_in_use = NO_CACHE_ID
        if self._kwargs.get(OFFSET, 0) == 0:
            self._next_id = None
            return

        first_cursor_kwargs = self._kwargs.copy()
        first_cursor_kwargs[OFFSET] = 0
        # offset may be too large, needed to seek in multiple times
        first_cursor_kwargs[LIMIT] = self._kwargs[OFFSET]
        first_cursor_kwargs[ITERATION_EXTENSION_REDUCE_RATE] = 0

        res = self._conn.query(self._collection_name, self._expr, self._output_fields, self._partition_names,
                               timeout=self._timeout, **first_cursor_kwargs)
        self.__update_cursor(res)
        self._kwargs[OFFSET] = 0

    def __maybe_cache(self, result):
        if len(result) < 2 * self._kwargs[LIMIT]:
            return
        start = self._kwargs[LIMIT]
        cache_result = result[start:]
        cache_id = iteratorCache.cache(cache_result, NO_CACHE_ID)
        self._cache_id_in_use = cache_id

    def __is_res_sufficient(self, res):
        return res is not None and len(res) >= self._kwargs[LIMIT]

    def next(self):
        cached_res = iteratorCache.fetch_cache(self._cache_id_in_use)
        ret = None
        if self.__is_res_sufficient(cached_res):
            ret = cached_res[0:self._kwargs[LIMIT]]
            res_to_cache = cached_res[self._kwargs[LIMIT]:]
            iteratorCache.cache(res_to_cache, self._cache_id_in_use)
        else:
            iteratorCache.release_cache(self._cache_id_in_use)
            current_expr = self.__setup_next_expr()
            res = self._conn.query(self._collection_name, current_expr, self._output_fields, self._partition_names,
                                   timeout=self._timeout, **self._kwargs)
            self.__maybe_cache(res)
            ret = res[0:min(self._kwargs[LIMIT], len(res))]
        self.__update_cursor(ret)
        return ret

    def __setup__pk_is_str(self):
        fields = self._schema[FIELDS]
        for field in fields:
            if field['is_primary']:
                if field['type'] == DataType.VARCHAR:
                    self._pk_str = True
                else:
                    self._pk_str = False
                break

    def __setup_next_expr(self):
        current_expr = self._expr
        if self._next_id is None:
            return current_expr
        if self._next_id is not None:
            if self._pk_str:
                current_expr = self._expr + f" and id > \"{self._next_id}\""
            else:
                current_expr = self._expr + f" and id > {self._next_id}"
        return current_expr

    def __update_cursor(self, res):
        if len(res) == 0:
            return
        self._next_id = res[-1][ID]

    def close(self):
        # release cache in use
        iteratorCache.release_cache(self._cache_id_in_use)


class SearchIterator:

    def __init__(self, connection, collection_name, data, ann_field, param, limit, expr=None, partition_names=None,
                 output_fields=None, timeout=None, round_decimal=-1, schema=None, **kwargs):
        if len(data) > 1:
            raise MilvusException("Not support multiple vector iterator at present")
        self._conn = connection
        self._iterator_params = {'collection_name': collection_name, "data": data,
                                 "ann_field": ann_field, "limit": limit,
                                 "output_fields": output_fields, "partition_names": partition_names,
                                 "timeout": timeout, "round_decimal": round_decimal}
        self._expr = expr
        self._param = param
        self._kwargs = kwargs
        self._distance_cursor = [0.0]
        self._filtered_ids = []
        self._schema = schema
        self.__check_radius()
        self.__seek()
        self.__setup__pk_is_str()

    def __setup__pk_is_str(self):
        fields = self._schema[FIELDS]
        for field in fields:
            if field['is_primary']:
                if field['type'] == DataType.VARCHAR:
                    self._pk_str = True
                else:
                    self._pk_str = False
                break

    def __check_radius(self):
        if self._param[PARAMS][RADIUS] is None:
            raise MilvusException(message="must provide radius parameter when using search iterator")

    def __seek(self):
        if self._kwargs.get(OFFSET, 0) != 0:
            raise MilvusException("Not support offset when searching iteration")

    def __update_cursor(self, res):
        if len(res[0]) == 0:
            return
        last_hit = res[0][-1]
        self._distance_cursor[0] = last_hit.distance
        self._filtered_ids = []
        for hit in res[0]:
            if hit.distance == last_hit.distance:
                self._filtered_ids.append(hit.id)

    def next(self):
        next_params = self.__next_params()
        next_expr = self.__filtered_duplicated_result_expr(self._expr)
        res = self._conn.search(self._iterator_params['collection_name'],
                                self._iterator_params['data'],
                                self._iterator_params['ann_field'],
                                next_params,
                                self._iterator_params['limit'],
                                next_expr,
                                self._iterator_params['partition_names'],
                                self._iterator_params['output_fields'],
                                self._iterator_params['round_decimal'],
                                timeout=self._iterator_params['timeout'],
                                schema=self._schema, **self._kwargs)
        self.__update_cursor(res)
        return res

    # at present, the range_filter parameter means 'larger/less and equal',
    # so there would be vectors with same distances returned multiple times in different pages
    # we need to refine and remove these results before returning
    def __filtered_duplicated_result_expr(self, expr):
        if len(self._filtered_ids) == 0:
            return expr

        filtered_ids_str = ""
        for filtered_id in self._filtered_ids:
            if self._pk_str:
                filtered_ids_str += f"\"{filtered_id}\", "
            else:
                filtered_ids_str += f"{filtered_id}, "

        filter_expr = f"id not in [{filtered_ids_str}]"
        if expr is not None:
            return expr + filter_expr
        return filter_expr

    def __next_params(self):
        next_params = self._param.copy()
        next_params[PARAMS][RANGE_FILTER] = self._distance_cursor[0]
        return next_params

    def close(self):
        pass


class IteratorCache:

    def __init__(self):
        self._cache_id = 0
        self._cache_map = {}

    def cache(self, result, cache_id):
        if cache_id == NO_CACHE_ID:
            self._cache_id += 1
            cache_id = self._cache_id
        self._cache_map[cache_id] = result
        return cache_id

    def fetch_cache(self, cache_id):
        return self._cache_map.get(cache_id, None)

    def release_cache(self, cache_id):
        if self._cache_map.get(cache_id, None) is not None:
            self._cache_map.pop(cache_id)


NO_CACHE_ID = -1
# Singleton Mode in Python
iteratorCache = IteratorCache()
