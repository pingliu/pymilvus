from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

Abnormal: StateCode
AllocateSegment: MsgType
AlterAlias: MsgType
AlterCollection: MsgType
BinaryVector: PlaceholderType
BoolExprV1: DslType
Bounded: ConsistencyLevel
BuildIndexError: ErrorCode
CacheFailed: ErrorCode
CannotCreateFile: ErrorCode
CannotCreateFolder: ErrorCode
CannotDeleteFile: ErrorCode
CannotDeleteFolder: ErrorCode
Collection: ObjectType
CollectionNameNotFound: ErrorCode
CollectionNotExists: ErrorCode
Completed: CompactionState
Connect: MsgType
ConnectFailed: ErrorCode
CreateAlias: MsgType
CreateCollection: MsgType
CreateCredential: MsgType
CreateCredentialFailure: ErrorCode
CreateIndex: MsgType
CreatePartition: MsgType
CreateResourceGroup: MsgType
CreateRole: MsgType
CreateRoleFailure: ErrorCode
Customized: ConsistencyLevel
DDRequestRace: ErrorCode
DESCRIPTOR: _descriptor.FileDescriptor
DataCoordNA: ErrorCode
DataNodeTt: MsgType
Delete: MsgType
DeleteCredential: MsgType
DeleteCredentialFailure: ErrorCode
DescribeAlias: MsgType
DescribeCollection: MsgType
DescribeIndex: MsgType
DescribePartition: MsgType
DescribeResourceGroup: MsgType
DescribeSegment: MsgType
DescribeSegments: MsgType
DiskQuotaExhausted: ErrorCode
DropAlias: MsgType
DropCollection: MsgType
DropIndex: MsgType
DropPartition: MsgType
DropResourceGroup: MsgType
DropRole: MsgType
DropRoleFailure: ErrorCode
Dropped: SegmentState
Dsl: DslType
EmptyCollection: ErrorCode
Eventually: ConsistencyLevel
Executing: CompactionState
Failed: IndexState
FederDescribeSegmentIndexData: MsgType
FederListIndexedSegment: MsgType
FileNotFound: ErrorCode
Finished: IndexState
FloatVector: PlaceholderType
Flush: MsgType
Flushed: SegmentState
Flushing: SegmentState
ForceDeny: ErrorCode
GetCollectionStatistics: MsgType
GetCredential: MsgType
GetCredentialFailure: ErrorCode
GetDistribution: MsgType
GetIndexBuildProgress: MsgType
GetIndexState: MsgType
GetIndexStatistics: MsgType
GetPartitionStatistics: MsgType
GetRecoveryInfo: MsgType
GetReplicas: MsgType
GetSegmentState: MsgType
GetShardLeaders: MsgType
GetSystemConfigs: MsgType
GetUserFailure: ErrorCode
Global: ObjectType
Growing: SegmentState
HandoffSegments: MsgType
HasCollection: MsgType
HasPartition: MsgType
Healthy: StateCode
IllegalArgument: ErrorCode
IllegalCollectionName: ErrorCode
IllegalDimension: ErrorCode
IllegalIndexType: ErrorCode
IllegalMetricType: ErrorCode
IllegalNLIST: ErrorCode
IllegalRowRecord: ErrorCode
IllegalSearchResult: ErrorCode
IllegalTOPK: ErrorCode
IllegalVectorID: ErrorCode
ImportCompleted: ImportState
ImportFailed: ImportState
ImportFailedAndCleaned: ImportState
ImportFlushed: ImportState
ImportPending: ImportState
ImportPersisted: ImportState
ImportStarted: ImportState
Importing: SegmentState
InProgress: IndexState
IndexNotExist: ErrorCode
IndexStateNone: IndexState
Initializing: StateCode
Insert: MsgType
InsufficientMemoryToLoad: ErrorCode
ListAliases: MsgType
ListClientInfos: MsgType
ListCredUsernames: MsgType
ListCredUsersFailure: ErrorCode
ListPolicy: MsgType
ListPolicyFailure: ErrorCode
ListResourceGroups: MsgType
LoadBalanceSegments: MsgType
LoadCollection: MsgType
LoadIndex: MsgType
LoadPartitions: MsgType
LoadSegments: MsgType
LoadStateLoaded: LoadState
LoadStateLoading: LoadState
LoadStateNotExist: LoadState
LoadStateNotLoad: LoadState
MemoryQuotaExhausted: ErrorCode
MetaFailed: ErrorCode
NoReplicaAvailable: ErrorCode
NodeIDNotMatch: ErrorCode
None: PlaceholderType
NotExist: SegmentState
NotReadyCoordActivating: ErrorCode
NotReadyServe: ErrorCode
NotShardLeader: ErrorCode
OperatePrivilege: MsgType
OperatePrivilegeFailure: ErrorCode
OperateUserRole: MsgType
OperateUserRoleFailure: ErrorCode
OutOfMemory: ErrorCode
PRIVILEGE_EXT_OBJ_FIELD_NUMBER: _ClassVar[int]
PermissionDenied: ErrorCode
PrivilegeAll: ObjectPrivilege
PrivilegeCompaction: ObjectPrivilege
PrivilegeCreateCollection: ObjectPrivilege
PrivilegeCreateIndex: ObjectPrivilege
PrivilegeCreateOwnership: ObjectPrivilege
PrivilegeCreateResourceGroup: ObjectPrivilege
PrivilegeDelete: ObjectPrivilege
PrivilegeDescribeCollection: ObjectPrivilege
PrivilegeDescribeResourceGroup: ObjectPrivilege
PrivilegeDropCollection: ObjectPrivilege
PrivilegeDropIndex: ObjectPrivilege
PrivilegeDropOwnership: ObjectPrivilege
PrivilegeDropResourceGroup: ObjectPrivilege
PrivilegeFlush: ObjectPrivilege
PrivilegeGetLoadState: ObjectPrivilege
PrivilegeGetLoadingProgress: ObjectPrivilege
PrivilegeGetStatistics: ObjectPrivilege
PrivilegeImport: ObjectPrivilege
PrivilegeIndexDetail: ObjectPrivilege
PrivilegeInsert: ObjectPrivilege
PrivilegeListResourceGroups: ObjectPrivilege
PrivilegeLoad: ObjectPrivilege
PrivilegeLoadBalance: ObjectPrivilege
PrivilegeManageOwnership: ObjectPrivilege
PrivilegeQuery: ObjectPrivilege
PrivilegeRelease: ObjectPrivilege
PrivilegeSearch: ObjectPrivilege
PrivilegeSelectOwnership: ObjectPrivilege
PrivilegeSelectUser: ObjectPrivilege
PrivilegeShowCollections: ObjectPrivilege
PrivilegeTransferNode: ObjectPrivilege
PrivilegeTransferReplica: ObjectPrivilege
PrivilegeUpdateUser: ObjectPrivilege
PrivilegeUpsert: ObjectPrivilege
QueryNodeStats: MsgType
RateLimit: ErrorCode
RefreshPolicyInfoCache: MsgType
RefreshPolicyInfoCacheFailure: ErrorCode
ReleaseCollection: MsgType
ReleasePartitions: MsgType
ReleaseSegments: MsgType
RemoveDmChannels: MsgType
RemoveQueryChannels: MsgType
RenameCollection: MsgType
RequestID: MsgType
RequestTSO: MsgType
ResendSegmentStats: MsgType
Retrieve: MsgType
RetrieveResult: MsgType
Retry: IndexState
Sealed: SegmentState
SealedSegmentsChangeInfo: MsgType
Search: MsgType
SearchResult: MsgType
SegmentFlushDone: MsgType
SegmentInfo: MsgType
SegmentNotFound: ErrorCode
SegmentStateNone: SegmentState
SegmentStatistics: MsgType
SelectGrant: MsgType
SelectGrantFailure: ErrorCode
SelectResource: MsgType
SelectResourceFailure: ErrorCode
SelectRole: MsgType
SelectRoleFailure: ErrorCode
SelectUser: MsgType
SelectUserFailure: ErrorCode
Session: ConsistencyLevel
ShowCollections: MsgType
ShowPartitions: MsgType
ShowSegments: MsgType
StandBy: StateCode
Stopping: StateCode
Strong: ConsistencyLevel
Success: ErrorCode
SyncDistribution: MsgType
SystemInfo: MsgType
TimeTick: MsgType
TimeTickLongDelay: ErrorCode
TransferNode: MsgType
TransferReplica: MsgType
UndefiedState: CompactionState
Undefined: MsgType
UnexpectedError: ErrorCode
Unissued: IndexState
UnsubDmChannel: MsgType
UpdateCredential: MsgType
UpdateCredentialFailure: ErrorCode
UpdateImportTaskFailure: ErrorCode
Upsert: MsgType
UpsertAutoIDTrue: ErrorCode
User: ObjectType
WatchDeltaChannels: MsgType
WatchDmChannels: MsgType
WatchQueryChannels: MsgType
privilege_ext_obj: _descriptor.FieldDescriptor

class Address(_message.Message):
    __slots__ = ["ip", "port"]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class Blob(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class ClientInfo(_message.Message):
    __slots__ = ["host", "local_time", "reserved", "sdk_type", "sdk_version", "user"]
    class ReservedEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HOST_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TIME_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    SDK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    host: str
    local_time: str
    reserved: _containers.ScalarMap[str, str]
    sdk_type: str
    sdk_version: str
    user: str
    def __init__(self, sdk_type: _Optional[str] = ..., sdk_version: _Optional[str] = ..., local_time: _Optional[str] = ..., user: _Optional[str] = ..., host: _Optional[str] = ..., reserved: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DMLMsgHeader(_message.Message):
    __slots__ = ["base", "shardName"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    SHARDNAME_FIELD_NUMBER: _ClassVar[int]
    base: MsgBase
    shardName: str
    def __init__(self, base: _Optional[_Union[MsgBase, _Mapping]] = ..., shardName: _Optional[str] = ...) -> None: ...

class KeyDataPair(_message.Message):
    __slots__ = ["data", "key"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    key: str
    def __init__(self, key: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class KeyValuePair(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class MsgBase(_message.Message):
    __slots__ = ["msgID", "msg_type", "sourceID", "targetID", "timestamp"]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCEID_FIELD_NUMBER: _ClassVar[int]
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    msgID: int
    msg_type: MsgType
    sourceID: int
    targetID: int
    timestamp: int
    def __init__(self, msg_type: _Optional[_Union[MsgType, str]] = ..., msgID: _Optional[int] = ..., timestamp: _Optional[int] = ..., sourceID: _Optional[int] = ..., targetID: _Optional[int] = ...) -> None: ...

class MsgHeader(_message.Message):
    __slots__ = ["base"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: MsgBase
    def __init__(self, base: _Optional[_Union[MsgBase, _Mapping]] = ...) -> None: ...

class PlaceholderGroup(_message.Message):
    __slots__ = ["placeholders"]
    PLACEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    placeholders: _containers.RepeatedCompositeFieldContainer[PlaceholderValue]
    def __init__(self, placeholders: _Optional[_Iterable[_Union[PlaceholderValue, _Mapping]]] = ...) -> None: ...

class PlaceholderValue(_message.Message):
    __slots__ = ["tag", "type", "values"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    tag: str
    type: PlaceholderType
    values: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, tag: _Optional[str] = ..., type: _Optional[_Union[PlaceholderType, str]] = ..., values: _Optional[_Iterable[bytes]] = ...) -> None: ...

class PrivilegeExt(_message.Message):
    __slots__ = ["object_name_index", "object_name_indexs", "object_privilege", "object_type"]
    OBJECT_NAME_INDEXS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_INDEX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_name_index: int
    object_name_indexs: int
    object_privilege: ObjectPrivilege
    object_type: ObjectType
    def __init__(self, object_type: _Optional[_Union[ObjectType, str]] = ..., object_privilege: _Optional[_Union[ObjectPrivilege, str]] = ..., object_name_index: _Optional[int] = ..., object_name_indexs: _Optional[int] = ...) -> None: ...

class SegmentStats(_message.Message):
    __slots__ = ["NumRows", "SegmentID"]
    NUMROWS_FIELD_NUMBER: _ClassVar[int]
    NumRows: int
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    SegmentID: int
    def __init__(self, SegmentID: _Optional[int] = ..., NumRows: _Optional[int] = ...) -> None: ...

class ServerInfo(_message.Message):
    __slots__ = ["build_tags", "build_time", "deploy_mode", "git_commit", "go_version", "reserved"]
    class ReservedEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BUILD_TAGS_FIELD_NUMBER: _ClassVar[int]
    BUILD_TIME_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_MODE_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMIT_FIELD_NUMBER: _ClassVar[int]
    GO_VERSION_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    build_tags: str
    build_time: str
    deploy_mode: str
    git_commit: str
    go_version: str
    reserved: _containers.ScalarMap[str, str]
    def __init__(self, build_tags: _Optional[str] = ..., build_time: _Optional[str] = ..., git_commit: _Optional[str] = ..., go_version: _Optional[str] = ..., deploy_mode: _Optional[str] = ..., reserved: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["code", "error_code", "reason"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    code: int
    error_code: ErrorCode
    reason: str
    def __init__(self, error_code: _Optional[_Union[ErrorCode, str]] = ..., reason: _Optional[str] = ..., code: _Optional[int] = ...) -> None: ...

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IndexState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SegmentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PlaceholderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DslType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CompactionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ConsistencyLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ImportState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ObjectPrivilege(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class StateCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class LoadState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
