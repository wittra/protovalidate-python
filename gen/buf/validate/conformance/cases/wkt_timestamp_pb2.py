# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/conformance/cases/wkt_timestamp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.protovalidate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n2buf/validate/conformance/cases/wkt_timestamp.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto"=\n\rTimestampNone\x12,\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03val"J\n\x11TimestampRequired\x12\x35\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x07\xfa\xf7\x18\x03\xc8\x01\x01R\x03val"K\n\x0eTimestampConst\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0b\xfa\xf7\x18\x07\xb2\x01\x04\x12\x02\x08\x03R\x03val"F\n\x0bTimestampLT\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\t\xfa\xf7\x18\x05\xb2\x01\x02\x1a\x00R\x03val"I\n\x0cTimestampLTE\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0b\xfa\xf7\x18\x07\xb2\x01\x04"\x02\x08\x01R\x03val"I\n\x0bTimestampGT\x12:\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0c\xfa\xf7\x18\x08\xb2\x01\x05*\x03\x10\xe8\x07R\x03val"K\n\x0cTimestampGTE\x12;\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xfa\xf7\x18\t\xb2\x01\x06\x32\x04\x10\xc0\x84=R\x03val"L\n\rTimestampGTLT\x12;\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xfa\xf7\x18\t\xb2\x01\x06\x1a\x02\x08\x01*\x00R\x03val"N\n\x0fTimestampExLTGT\x12;\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xfa\xf7\x18\t\xb2\x01\x06\x1a\x00*\x02\x08\x01R\x03val"Q\n\x0fTimestampGTELTE\x12>\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x10\xfa\xf7\x18\x0c\xb2\x01\t"\x03\x08\x90\x1c\x32\x02\x08<R\x03val"S\n\x11TimestampExGTELTE\x12>\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x10\xfa\xf7\x18\x0c\xb2\x01\t"\x02\x08<2\x03\x08\x90\x1cR\x03val"I\n\x0eTimestampLTNow\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\t\xfa\xf7\x18\x05\xb2\x01\x02\x38\x01R\x03val"I\n\x0eTimestampGTNow\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\t\xfa\xf7\x18\x05\xb2\x01\x02@\x01R\x03val"M\n\x0fTimestampWithin\x12:\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0c\xfa\xf7\x18\x08\xb2\x01\x05J\x03\x08\x90\x1cR\x03val"T\n\x14TimestampLTNowWithin\x12<\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0e\xfa\xf7\x18\n\xb2\x01\x07\x38\x01J\x03\x08\x90\x1cR\x03val"T\n\x14TimestampGTNowWithin\x12<\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0e\xfa\xf7\x18\n\xb2\x01\x07@\x01J\x03\x08\x90\x1cR\x03valb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "buf.validate.conformance.cases.wkt_timestamp_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TIMESTAMPREQUIRED.fields_by_name["val"]._options = None
    _TIMESTAMPREQUIRED.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\003\310\001\001"
    _TIMESTAMPCONST.fields_by_name["val"]._options = None
    _TIMESTAMPCONST.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\007\262\001\004\022\002\010\003"
    _TIMESTAMPLT.fields_by_name["val"]._options = None
    _TIMESTAMPLT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\262\001\002\032\000"
    _TIMESTAMPLTE.fields_by_name["val"]._options = None
    _TIMESTAMPLTE.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\007\262\001\004"\002\010\001'
    _TIMESTAMPGT.fields_by_name["val"]._options = None
    _TIMESTAMPGT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\010\262\001\005*\003\020\350\007"
    _TIMESTAMPGTE.fields_by_name["val"]._options = None
    _TIMESTAMPGTE.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\t\262\001\0062\004\020\300\204="
    _TIMESTAMPGTLT.fields_by_name["val"]._options = None
    _TIMESTAMPGTLT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\t\262\001\006\032\002\010\001*\000"
    _TIMESTAMPEXLTGT.fields_by_name["val"]._options = None
    _TIMESTAMPEXLTGT.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\t\262\001\006\032\000*\002\010\001"
    _TIMESTAMPGTELTE.fields_by_name["val"]._options = None
    _TIMESTAMPGTELTE.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\014\262\001\t"\003\010\220\0342\002\010<'
    _TIMESTAMPEXGTELTE.fields_by_name["val"]._options = None
    _TIMESTAMPEXGTELTE.fields_by_name[
        "val"
    ]._serialized_options = b'\372\367\030\014\262\001\t"\002\010<2\003\010\220\034'
    _TIMESTAMPLTNOW.fields_by_name["val"]._options = None
    _TIMESTAMPLTNOW.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\262\001\0028\001"
    _TIMESTAMPGTNOW.fields_by_name["val"]._options = None
    _TIMESTAMPGTNOW.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\005\262\001\002@\001"
    _TIMESTAMPWITHIN.fields_by_name["val"]._options = None
    _TIMESTAMPWITHIN.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\010\262\001\005J\003\010\220\034"
    _TIMESTAMPLTNOWWITHIN.fields_by_name["val"]._options = None
    _TIMESTAMPLTNOWWITHIN.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\n\262\001\0078\001J\003\010\220\034"
    _TIMESTAMPGTNOWWITHIN.fields_by_name["val"]._options = None
    _TIMESTAMPGTNOWWITHIN.fields_by_name[
        "val"
    ]._serialized_options = b"\372\367\030\n\262\001\007@\001J\003\010\220\034"
    _globals["_TIMESTAMPNONE"]._serialized_start = 148
    _globals["_TIMESTAMPNONE"]._serialized_end = 209
    _globals["_TIMESTAMPREQUIRED"]._serialized_start = 211
    _globals["_TIMESTAMPREQUIRED"]._serialized_end = 285
    _globals["_TIMESTAMPCONST"]._serialized_start = 287
    _globals["_TIMESTAMPCONST"]._serialized_end = 362
    _globals["_TIMESTAMPLT"]._serialized_start = 364
    _globals["_TIMESTAMPLT"]._serialized_end = 434
    _globals["_TIMESTAMPLTE"]._serialized_start = 436
    _globals["_TIMESTAMPLTE"]._serialized_end = 509
    _globals["_TIMESTAMPGT"]._serialized_start = 511
    _globals["_TIMESTAMPGT"]._serialized_end = 584
    _globals["_TIMESTAMPGTE"]._serialized_start = 586
    _globals["_TIMESTAMPGTE"]._serialized_end = 661
    _globals["_TIMESTAMPGTLT"]._serialized_start = 663
    _globals["_TIMESTAMPGTLT"]._serialized_end = 739
    _globals["_TIMESTAMPEXLTGT"]._serialized_start = 741
    _globals["_TIMESTAMPEXLTGT"]._serialized_end = 819
    _globals["_TIMESTAMPGTELTE"]._serialized_start = 821
    _globals["_TIMESTAMPGTELTE"]._serialized_end = 902
    _globals["_TIMESTAMPEXGTELTE"]._serialized_start = 904
    _globals["_TIMESTAMPEXGTELTE"]._serialized_end = 987
    _globals["_TIMESTAMPLTNOW"]._serialized_start = 989
    _globals["_TIMESTAMPLTNOW"]._serialized_end = 1062
    _globals["_TIMESTAMPGTNOW"]._serialized_start = 1064
    _globals["_TIMESTAMPGTNOW"]._serialized_end = 1137
    _globals["_TIMESTAMPWITHIN"]._serialized_start = 1139
    _globals["_TIMESTAMPWITHIN"]._serialized_end = 1216
    _globals["_TIMESTAMPLTNOWWITHIN"]._serialized_start = 1218
    _globals["_TIMESTAMPLTNOWWITHIN"]._serialized_end = 1302
    _globals["_TIMESTAMPGTNOWWITHIN"]._serialized_start = 1304
    _globals["_TIMESTAMPGTNOWWITHIN"]._serialized_end = 1388
# @@protoc_insertion_point(module_scope)
