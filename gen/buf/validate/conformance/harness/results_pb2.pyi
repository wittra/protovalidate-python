from buf.validate.conformance.harness import harness_pb2 as _harness_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResultOptions(_message.Message):
    __slots__ = ["suite_filter", "case_filter", "verbose", "strict", "strict_message", "strict_error"]
    SUITE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CASE_FILTER_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    STRICT_FIELD_NUMBER: _ClassVar[int]
    STRICT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STRICT_ERROR_FIELD_NUMBER: _ClassVar[int]
    suite_filter: str
    case_filter: str
    verbose: bool
    strict: bool
    strict_message: bool
    strict_error: bool
    def __init__(self, suite_filter: _Optional[str] = ..., case_filter: _Optional[str] = ..., verbose: bool = ..., strict: bool = ..., strict_message: bool = ..., strict_error: bool = ...) -> None: ...

class ResultSet(_message.Message):
    __slots__ = ["successes", "failures", "suites", "options"]
    SUCCESSES_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    SUITES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    successes: int
    failures: int
    suites: _containers.RepeatedCompositeFieldContainer[SuiteResults]
    options: ResultOptions
    def __init__(self, successes: _Optional[int] = ..., failures: _Optional[int] = ..., suites: _Optional[_Iterable[_Union[SuiteResults, _Mapping]]] = ..., options: _Optional[_Union[ResultOptions, _Mapping]] = ...) -> None: ...

class SuiteResults(_message.Message):
    __slots__ = ["name", "successes", "failures", "cases", "fdset"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESSES_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    CASES_FIELD_NUMBER: _ClassVar[int]
    FDSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    successes: int
    failures: int
    cases: _containers.RepeatedCompositeFieldContainer[CaseResult]
    fdset: _descriptor_pb2.FileDescriptorSet
    def __init__(self, name: _Optional[str] = ..., successes: _Optional[int] = ..., failures: _Optional[int] = ..., cases: _Optional[_Iterable[_Union[CaseResult, _Mapping]]] = ..., fdset: _Optional[_Union[_descriptor_pb2.FileDescriptorSet, _Mapping]] = ...) -> None: ...

class CaseResult(_message.Message):
    __slots__ = ["name", "success", "wanted", "got", "input"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    WANTED_FIELD_NUMBER: _ClassVar[int]
    GOT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    name: str
    success: bool
    wanted: _harness_pb2.TestResult
    got: _harness_pb2.TestResult
    input: _any_pb2.Any
    def __init__(self, name: _Optional[str] = ..., success: bool = ..., wanted: _Optional[_Union[_harness_pb2.TestResult, _Mapping]] = ..., got: _Optional[_Union[_harness_pb2.TestResult, _Mapping]] = ..., input: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
