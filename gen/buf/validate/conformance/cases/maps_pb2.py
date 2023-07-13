# Copyright 2023 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/conformance/cases/maps.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)buf/validate/conformance/cases/maps.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x1b\x62uf/validate/validate.proto\"\x85\x01\n\x07MapNone\x12\x42\n\x03val\x18\x01 \x03(\x0b\x32\x30.buf.validate.conformance.cases.MapNone.ValEntryR\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\rR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\"\x8d\x01\n\x06MapMin\x12K\n\x03val\x18\x01 \x03(\x0b\x32/.buf.validate.conformance.cases.MapMin.ValEntryB\x08\xbaH\x05\x9a\x01\x02\x08\x02R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x02R\x05value:\x02\x38\x01\"\x8d\x01\n\x06MapMax\x12K\n\x03val\x18\x01 \x03(\x0b\x32/.buf.validate.conformance.cases.MapMax.ValEntryB\x08\xbaH\x05\x9a\x01\x02\x10\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value:\x02\x38\x01\"\x95\x01\n\tMapMinMax\x12P\n\x03val\x18\x01 \x03(\x0b\x32\x32.buf.validate.conformance.cases.MapMinMax.ValEntryB\n\xbaH\x07\x9a\x01\x04\x08\x02\x10\x04R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\"\x93\x01\n\x08MapExact\x12O\n\x03val\x18\x01 \x03(\x0b\x32\x31.buf.validate.conformance.cases.MapExact.ValEntryB\n\xbaH\x07\x9a\x01\x04\x08\x03\x10\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x04R\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x93\x01\n\x07MapKeys\x12P\n\x03val\x18\x01 \x03(\x0b\x32\x30.buf.validate.conformance.cases.MapKeys.ValEntryB\x0c\xbaH\t\x9a\x01\x06\"\x04\x42\x02\x10\x00R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x12R\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x97\x01\n\tMapValues\x12R\n\x03val\x18\x01 \x03(\x0b\x32\x32.buf.validate.conformance.cases.MapValues.ValEntryB\x0c\xbaH\t\x9a\x01\x06*\x04r\x02\x10\x03R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xb0\x01\n\x0eMapKeysPattern\x12\x66\n\x03val\x18\x01 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MapKeysPattern.ValEntryB\x1b\xbaH\x18\x9a\x01\x15\"\x13r\x11\x32\x0f(?i)^[a-z0-9]+$R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xb4\x01\n\x10MapValuesPattern\x12h\n\x03val\x18\x01 \x03(\x0b\x32\x39.buf.validate.conformance.cases.MapValuesPattern.ValEntryB\x1b\xbaH\x18\x9a\x01\x15*\x13r\x11\x32\x0f(?i)^[a-z0-9]+$R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xe3\x01\n\x0cMapRecursive\x12G\n\x03val\x18\x01 \x03(\x0b\x32\x35.buf.validate.conformance.cases.MapRecursive.ValEntryR\x03val\x1ah\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\rR\x03key\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x30.buf.validate.conformance.cases.MapRecursive.MsgR\x05value:\x02\x38\x01\x1a \n\x03Msg\x12\x19\n\x03val\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x03R\x03val\"\xa2\x01\n\x0eMapExactIgnore\x12X\n\x03val\x18\x01 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MapExactIgnore.ValEntryB\r\xbaH\n\x9a\x01\x04\x08\x03\x10\x03\xd0\x01\x01R\x03val\x1a\x36\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\x04R\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xd7\x03\n\x0cMultipleMaps\x12[\n\x05\x66irst\x18\x01 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MultipleMaps.FirstEntryB\x0c\xbaH\t\x9a\x01\x06\"\x04*\x02 \x00R\x05\x66irst\x12^\n\x06second\x18\x02 \x03(\x0b\x32\x38.buf.validate.conformance.cases.MultipleMaps.SecondEntryB\x0c\xbaH\t\x9a\x01\x06\"\x04\x1a\x02\x10\x00R\x06second\x12[\n\x05third\x18\x03 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MultipleMaps.ThirdEntryB\x0c\xbaH\t\x9a\x01\x06\"\x04\x1a\x02 \x00R\x05third\x1a\x38\n\nFirstEntry\x12\x10\n\x03key\x18\x01 \x01(\rR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x39\n\x0bSecondEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\x1a\x38\n\nThirdEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.maps_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAPNONE_VALENTRY._options = None
  _MAPNONE_VALENTRY._serialized_options = b'8\001'
  _MAPMIN_VALENTRY._options = None
  _MAPMIN_VALENTRY._serialized_options = b'8\001'
  _MAPMIN.fields_by_name['val']._options = None
  _MAPMIN.fields_by_name['val']._serialized_options = b'\272H\005\232\001\002\010\002'
  _MAPMAX_VALENTRY._options = None
  _MAPMAX_VALENTRY._serialized_options = b'8\001'
  _MAPMAX.fields_by_name['val']._options = None
  _MAPMAX.fields_by_name['val']._serialized_options = b'\272H\005\232\001\002\020\003'
  _MAPMINMAX_VALENTRY._options = None
  _MAPMINMAX_VALENTRY._serialized_options = b'8\001'
  _MAPMINMAX.fields_by_name['val']._options = None
  _MAPMINMAX.fields_by_name['val']._serialized_options = b'\272H\007\232\001\004\010\002\020\004'
  _MAPEXACT_VALENTRY._options = None
  _MAPEXACT_VALENTRY._serialized_options = b'8\001'
  _MAPEXACT.fields_by_name['val']._options = None
  _MAPEXACT.fields_by_name['val']._serialized_options = b'\272H\007\232\001\004\010\003\020\003'
  _MAPKEYS_VALENTRY._options = None
  _MAPKEYS_VALENTRY._serialized_options = b'8\001'
  _MAPKEYS.fields_by_name['val']._options = None
  _MAPKEYS.fields_by_name['val']._serialized_options = b'\272H\t\232\001\006\"\004B\002\020\000'
  _MAPVALUES_VALENTRY._options = None
  _MAPVALUES_VALENTRY._serialized_options = b'8\001'
  _MAPVALUES.fields_by_name['val']._options = None
  _MAPVALUES.fields_by_name['val']._serialized_options = b'\272H\t\232\001\006*\004r\002\020\003'
  _MAPKEYSPATTERN_VALENTRY._options = None
  _MAPKEYSPATTERN_VALENTRY._serialized_options = b'8\001'
  _MAPKEYSPATTERN.fields_by_name['val']._options = None
  _MAPKEYSPATTERN.fields_by_name['val']._serialized_options = b'\272H\030\232\001\025\"\023r\0212\017(?i)^[a-z0-9]+$'
  _MAPVALUESPATTERN_VALENTRY._options = None
  _MAPVALUESPATTERN_VALENTRY._serialized_options = b'8\001'
  _MAPVALUESPATTERN.fields_by_name['val']._options = None
  _MAPVALUESPATTERN.fields_by_name['val']._serialized_options = b'\272H\030\232\001\025*\023r\0212\017(?i)^[a-z0-9]+$'
  _MAPRECURSIVE_VALENTRY._options = None
  _MAPRECURSIVE_VALENTRY._serialized_options = b'8\001'
  _MAPRECURSIVE_MSG.fields_by_name['val']._options = None
  _MAPRECURSIVE_MSG.fields_by_name['val']._serialized_options = b'\272H\004r\002\020\003'
  _MAPEXACTIGNORE_VALENTRY._options = None
  _MAPEXACTIGNORE_VALENTRY._serialized_options = b'8\001'
  _MAPEXACTIGNORE.fields_by_name['val']._options = None
  _MAPEXACTIGNORE.fields_by_name['val']._serialized_options = b'\272H\n\232\001\004\010\003\020\003\320\001\001'
  _MULTIPLEMAPS_FIRSTENTRY._options = None
  _MULTIPLEMAPS_FIRSTENTRY._serialized_options = b'8\001'
  _MULTIPLEMAPS_SECONDENTRY._options = None
  _MULTIPLEMAPS_SECONDENTRY._serialized_options = b'8\001'
  _MULTIPLEMAPS_THIRDENTRY._options = None
  _MULTIPLEMAPS_THIRDENTRY._serialized_options = b'8\001'
  _MULTIPLEMAPS.fields_by_name['first']._options = None
  _MULTIPLEMAPS.fields_by_name['first']._serialized_options = b'\272H\t\232\001\006\"\004*\002 \000'
  _MULTIPLEMAPS.fields_by_name['second']._options = None
  _MULTIPLEMAPS.fields_by_name['second']._serialized_options = b'\272H\t\232\001\006\"\004\032\002\020\000'
  _MULTIPLEMAPS.fields_by_name['third']._options = None
  _MULTIPLEMAPS.fields_by_name['third']._serialized_options = b'\272H\t\232\001\006\"\004\032\002 \000'
  _globals['_MAPNONE']._serialized_start=107
  _globals['_MAPNONE']._serialized_end=240
  _globals['_MAPNONE_VALENTRY']._serialized_start=186
  _globals['_MAPNONE_VALENTRY']._serialized_end=240
  _globals['_MAPMIN']._serialized_start=243
  _globals['_MAPMIN']._serialized_end=384
  _globals['_MAPMIN_VALENTRY']._serialized_start=330
  _globals['_MAPMIN_VALENTRY']._serialized_end=384
  _globals['_MAPMAX']._serialized_start=387
  _globals['_MAPMAX']._serialized_end=528
  _globals['_MAPMAX_VALENTRY']._serialized_start=474
  _globals['_MAPMAX_VALENTRY']._serialized_end=528
  _globals['_MAPMINMAX']._serialized_start=531
  _globals['_MAPMINMAX']._serialized_end=680
  _globals['_MAPMINMAX_VALENTRY']._serialized_start=626
  _globals['_MAPMINMAX_VALENTRY']._serialized_end=680
  _globals['_MAPEXACT']._serialized_start=683
  _globals['_MAPEXACT']._serialized_end=830
  _globals['_MAPEXACT_VALENTRY']._serialized_start=776
  _globals['_MAPEXACT_VALENTRY']._serialized_end=830
  _globals['_MAPKEYS']._serialized_start=833
  _globals['_MAPKEYS']._serialized_end=980
  _globals['_MAPKEYS_VALENTRY']._serialized_start=926
  _globals['_MAPKEYS_VALENTRY']._serialized_end=980
  _globals['_MAPVALUES']._serialized_start=983
  _globals['_MAPVALUES']._serialized_end=1134
  _globals['_MAPVALUES_VALENTRY']._serialized_start=1080
  _globals['_MAPVALUES_VALENTRY']._serialized_end=1134
  _globals['_MAPKEYSPATTERN']._serialized_start=1137
  _globals['_MAPKEYSPATTERN']._serialized_end=1313
  _globals['_MAPKEYSPATTERN_VALENTRY']._serialized_start=1080
  _globals['_MAPKEYSPATTERN_VALENTRY']._serialized_end=1134
  _globals['_MAPVALUESPATTERN']._serialized_start=1316
  _globals['_MAPVALUESPATTERN']._serialized_end=1496
  _globals['_MAPVALUESPATTERN_VALENTRY']._serialized_start=1080
  _globals['_MAPVALUESPATTERN_VALENTRY']._serialized_end=1134
  _globals['_MAPRECURSIVE']._serialized_start=1499
  _globals['_MAPRECURSIVE']._serialized_end=1726
  _globals['_MAPRECURSIVE_VALENTRY']._serialized_start=1588
  _globals['_MAPRECURSIVE_VALENTRY']._serialized_end=1692
  _globals['_MAPRECURSIVE_MSG']._serialized_start=1694
  _globals['_MAPRECURSIVE_MSG']._serialized_end=1726
  _globals['_MAPEXACTIGNORE']._serialized_start=1729
  _globals['_MAPEXACTIGNORE']._serialized_end=1891
  _globals['_MAPEXACTIGNORE_VALENTRY']._serialized_start=776
  _globals['_MAPEXACTIGNORE_VALENTRY']._serialized_end=830
  _globals['_MULTIPLEMAPS']._serialized_start=1894
  _globals['_MULTIPLEMAPS']._serialized_end=2365
  _globals['_MULTIPLEMAPS_FIRSTENTRY']._serialized_start=2192
  _globals['_MULTIPLEMAPS_FIRSTENTRY']._serialized_end=2248
  _globals['_MULTIPLEMAPS_SECONDENTRY']._serialized_start=2250
  _globals['_MULTIPLEMAPS_SECONDENTRY']._serialized_end=2307
  _globals['_MULTIPLEMAPS_THIRDENTRY']._serialized_start=2309
  _globals['_MULTIPLEMAPS_THIRDENTRY']._serialized_end=2365
# @@protoc_insertion_point(module_scope)
