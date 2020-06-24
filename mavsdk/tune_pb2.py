# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tune/tune.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tune/tune.proto',
  package='mavsdk.rpc.tune',
  syntax='proto3',
  serialized_options=b'\n\016io.mavsdk.tuneB\tTuneProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0ftune/tune.proto\x12\x0fmavsdk.rpc.tune\x1a\x14mavsdk_options.proto\"H\n\x0fPlayTuneRequest\x12\x35\n\x0b\x64\x65scription\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.tune.TuneDescription\"D\n\x10PlayTuneResponse\x12\x30\n\x0btune_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.tune.TuneResult\"U\n\x0fTuneDescription\x12\x33\n\rsong_elements\x18\x01 \x03(\x0e\x32\x1c.mavsdk.rpc.tune.SongElement\x12\r\n\x05tempo\x18\x02 \x01(\x05\"\xcc\x01\n\nTuneResult\x12\x32\n\x06result\x18\x01 \x01(\x0e\x32\".mavsdk.rpc.tune.TuneResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"v\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x18\n\x14RESULT_INVALID_TEMPO\x10\x02\x12\x18\n\x14RESULT_TUNE_TOO_LONG\x10\x03\x12\x10\n\x0cRESULT_ERROR\x10\x04*\xd1\x04\n\x0bSongElement\x12\x1d\n\x19SONG_ELEMENT_STYLE_LEGATO\x10\x00\x12\x1d\n\x19SONG_ELEMENT_STYLE_NORMAL\x10\x01\x12\x1f\n\x1bSONG_ELEMENT_STYLE_STACCATO\x10\x02\x12\x1b\n\x17SONG_ELEMENT_DURATION_1\x10\x03\x12\x1b\n\x17SONG_ELEMENT_DURATION_2\x10\x04\x12\x1b\n\x17SONG_ELEMENT_DURATION_4\x10\x05\x12\x1b\n\x17SONG_ELEMENT_DURATION_8\x10\x06\x12\x1c\n\x18SONG_ELEMENT_DURATION_16\x10\x07\x12\x1c\n\x18SONG_ELEMENT_DURATION_32\x10\x08\x12\x17\n\x13SONG_ELEMENT_NOTE_A\x10\t\x12\x17\n\x13SONG_ELEMENT_NOTE_B\x10\n\x12\x17\n\x13SONG_ELEMENT_NOTE_C\x10\x0b\x12\x17\n\x13SONG_ELEMENT_NOTE_D\x10\x0c\x12\x17\n\x13SONG_ELEMENT_NOTE_E\x10\r\x12\x17\n\x13SONG_ELEMENT_NOTE_F\x10\x0e\x12\x17\n\x13SONG_ELEMENT_NOTE_G\x10\x0f\x12\x1b\n\x17SONG_ELEMENT_NOTE_PAUSE\x10\x10\x12\x16\n\x12SONG_ELEMENT_SHARP\x10\x11\x12\x15\n\x11SONG_ELEMENT_FLAT\x10\x12\x12\x1a\n\x16SONG_ELEMENT_OCTAVE_UP\x10\x13\x12\x1c\n\x18SONG_ELEMENT_OCTAVE_DOWN\x10\x14\x32`\n\x0bTuneService\x12Q\n\x08PlayTune\x12 .mavsdk.rpc.tune.PlayTuneRequest\x1a!.mavsdk.rpc.tune.PlayTuneResponse\"\x00\x42\x1b\n\x0eio.mavsdk.tuneB\tTuneProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])

_SONGELEMENT = _descriptor.EnumDescriptor(
  name='SongElement',
  full_name='mavsdk.rpc.tune.SongElement',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_STYLE_LEGATO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_STYLE_NORMAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_STYLE_STACCATO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_DURATION_1', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_DURATION_2', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_DURATION_4', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_DURATION_8', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_DURATION_16', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_DURATION_32', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_NOTE_A', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_NOTE_B', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_NOTE_C', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_NOTE_D', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_NOTE_E', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_NOTE_F', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_NOTE_G', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_NOTE_PAUSE', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_SHARP', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_FLAT', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_OCTAVE_UP', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SONG_ELEMENT_OCTAVE_DOWN', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=497,
  serialized_end=1090,
)
_sym_db.RegisterEnumDescriptor(_SONGELEMENT)

SongElement = enum_type_wrapper.EnumTypeWrapper(_SONGELEMENT)
SONG_ELEMENT_STYLE_LEGATO = 0
SONG_ELEMENT_STYLE_NORMAL = 1
SONG_ELEMENT_STYLE_STACCATO = 2
SONG_ELEMENT_DURATION_1 = 3
SONG_ELEMENT_DURATION_2 = 4
SONG_ELEMENT_DURATION_4 = 5
SONG_ELEMENT_DURATION_8 = 6
SONG_ELEMENT_DURATION_16 = 7
SONG_ELEMENT_DURATION_32 = 8
SONG_ELEMENT_NOTE_A = 9
SONG_ELEMENT_NOTE_B = 10
SONG_ELEMENT_NOTE_C = 11
SONG_ELEMENT_NOTE_D = 12
SONG_ELEMENT_NOTE_E = 13
SONG_ELEMENT_NOTE_F = 14
SONG_ELEMENT_NOTE_G = 15
SONG_ELEMENT_NOTE_PAUSE = 16
SONG_ELEMENT_SHARP = 17
SONG_ELEMENT_FLAT = 18
SONG_ELEMENT_OCTAVE_UP = 19
SONG_ELEMENT_OCTAVE_DOWN = 20


_TUNERESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.tune.TuneResult.Result',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_INVALID_TEMPO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TUNE_TOO_LONG', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=376,
  serialized_end=494,
)
_sym_db.RegisterEnumDescriptor(_TUNERESULT_RESULT)


_PLAYTUNEREQUEST = _descriptor.Descriptor(
  name='PlayTuneRequest',
  full_name='mavsdk.rpc.tune.PlayTuneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='mavsdk.rpc.tune.PlayTuneRequest.description', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=130,
)


_PLAYTUNERESPONSE = _descriptor.Descriptor(
  name='PlayTuneResponse',
  full_name='mavsdk.rpc.tune.PlayTuneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tune_result', full_name='mavsdk.rpc.tune.PlayTuneResponse.tune_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=200,
)


_TUNEDESCRIPTION = _descriptor.Descriptor(
  name='TuneDescription',
  full_name='mavsdk.rpc.tune.TuneDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='song_elements', full_name='mavsdk.rpc.tune.TuneDescription.song_elements', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tempo', full_name='mavsdk.rpc.tune.TuneDescription.tempo', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=287,
)


_TUNERESULT = _descriptor.Descriptor(
  name='TuneResult',
  full_name='mavsdk.rpc.tune.TuneResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.tune.TuneResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.tune.TuneResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TUNERESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=494,
)

_PLAYTUNEREQUEST.fields_by_name['description'].message_type = _TUNEDESCRIPTION
_PLAYTUNERESPONSE.fields_by_name['tune_result'].message_type = _TUNERESULT
_TUNEDESCRIPTION.fields_by_name['song_elements'].enum_type = _SONGELEMENT
_TUNERESULT.fields_by_name['result'].enum_type = _TUNERESULT_RESULT
_TUNERESULT_RESULT.containing_type = _TUNERESULT
DESCRIPTOR.message_types_by_name['PlayTuneRequest'] = _PLAYTUNEREQUEST
DESCRIPTOR.message_types_by_name['PlayTuneResponse'] = _PLAYTUNERESPONSE
DESCRIPTOR.message_types_by_name['TuneDescription'] = _TUNEDESCRIPTION
DESCRIPTOR.message_types_by_name['TuneResult'] = _TUNERESULT
DESCRIPTOR.enum_types_by_name['SongElement'] = _SONGELEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayTuneRequest = _reflection.GeneratedProtocolMessageType('PlayTuneRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLAYTUNEREQUEST,
  '__module__' : 'tune.tune_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.tune.PlayTuneRequest)
  })
_sym_db.RegisterMessage(PlayTuneRequest)

PlayTuneResponse = _reflection.GeneratedProtocolMessageType('PlayTuneResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLAYTUNERESPONSE,
  '__module__' : 'tune.tune_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.tune.PlayTuneResponse)
  })
_sym_db.RegisterMessage(PlayTuneResponse)

TuneDescription = _reflection.GeneratedProtocolMessageType('TuneDescription', (_message.Message,), {
  'DESCRIPTOR' : _TUNEDESCRIPTION,
  '__module__' : 'tune.tune_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.tune.TuneDescription)
  })
_sym_db.RegisterMessage(TuneDescription)

TuneResult = _reflection.GeneratedProtocolMessageType('TuneResult', (_message.Message,), {
  'DESCRIPTOR' : _TUNERESULT,
  '__module__' : 'tune.tune_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.tune.TuneResult)
  })
_sym_db.RegisterMessage(TuneResult)


DESCRIPTOR._options = None

_TUNESERVICE = _descriptor.ServiceDescriptor(
  name='TuneService',
  full_name='mavsdk.rpc.tune.TuneService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1092,
  serialized_end=1188,
  methods=[
  _descriptor.MethodDescriptor(
    name='PlayTune',
    full_name='mavsdk.rpc.tune.TuneService.PlayTune',
    index=0,
    containing_service=None,
    input_type=_PLAYTUNEREQUEST,
    output_type=_PLAYTUNERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TUNESERVICE)

DESCRIPTOR.services_by_name['TuneService'] = _TUNESERVICE

# @@protoc_insertion_point(module_scope)
