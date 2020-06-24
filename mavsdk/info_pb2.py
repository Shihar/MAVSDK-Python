# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: info/info.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='info/info.proto',
  package='mavsdk.rpc.info',
  syntax='proto3',
  serialized_options=b'\n\016io.mavsdk.infoB\tInfoProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0finfo/info.proto\x12\x0fmavsdk.rpc.info\x1a\x14mavsdk_options.proto\"\x1d\n\x1bGetFlightInformationRequest\"\x82\x01\n\x1cGetFlightInformationResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12\x30\n\x0b\x66light_info\x18\x02 \x01(\x0b\x32\x1b.mavsdk.rpc.info.FlightInfo\"\x1a\n\x18GetIdentificationRequest\"\x86\x01\n\x19GetIdentificationResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12\x37\n\x0eidentification\x18\x02 \x01(\x0b\x32\x1f.mavsdk.rpc.info.Identification\"\x13\n\x11GetProductRequest\"q\n\x12GetProductResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12)\n\x07product\x18\x02 \x01(\x0b\x32\x18.mavsdk.rpc.info.Product\"\x13\n\x11GetVersionRequest\"q\n\x12GetVersionResponse\x12\x30\n\x0binfo_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.info.InfoResult\x12)\n\x07version\x18\x02 \x01(\x0b\x32\x18.mavsdk.rpc.info.Version\"6\n\nFlightInfo\x12\x14\n\x0ctime_boot_ms\x18\x01 \x01(\r\x12\x12\n\nflight_uid\x18\x02 \x01(\x04\"&\n\x0eIdentification\x12\x14\n\x0chardware_uid\x18\x01 \x01(\t\"[\n\x07Product\x12\x11\n\tvendor_id\x18\x01 \x01(\x05\x12\x13\n\x0bvendor_name\x18\x02 \x01(\t\x12\x12\n\nproduct_id\x18\x03 \x01(\x05\x12\x14\n\x0cproduct_name\x18\x04 \x01(\t\"\xa7\x02\n\x07Version\x12\x17\n\x0f\x66light_sw_major\x18\x01 \x01(\x05\x12\x17\n\x0f\x66light_sw_minor\x18\x02 \x01(\x05\x12\x17\n\x0f\x66light_sw_patch\x18\x03 \x01(\x05\x12\x1e\n\x16\x66light_sw_vendor_major\x18\x04 \x01(\x05\x12\x1e\n\x16\x66light_sw_vendor_minor\x18\x05 \x01(\x05\x12\x1e\n\x16\x66light_sw_vendor_patch\x18\x06 \x01(\x05\x12\x13\n\x0bos_sw_major\x18\x07 \x01(\x05\x12\x13\n\x0bos_sw_minor\x18\x08 \x01(\x05\x12\x13\n\x0bos_sw_patch\x18\t \x01(\x05\x12\x1a\n\x12\x66light_sw_git_hash\x18\n \x01(\t\x12\x16\n\x0eos_sw_git_hash\x18\x0b \x01(\t\"\xaf\x01\n\nInfoResult\x12\x32\n\x06result\x18\x01 \x01(\x0e\x32\".mavsdk.rpc.info.InfoResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"Y\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\'\n#RESULT_INFORMATION_NOT_RECEIVED_YET\x10\x02\x32\xb4\x03\n\x0bInfoService\x12y\n\x14GetFlightInformation\x12,.mavsdk.rpc.info.GetFlightInformationRequest\x1a-.mavsdk.rpc.info.GetFlightInformationResponse\"\x04\x80\xb5\x18\x01\x12p\n\x11GetIdentification\x12).mavsdk.rpc.info.GetIdentificationRequest\x1a*.mavsdk.rpc.info.GetIdentificationResponse\"\x04\x80\xb5\x18\x01\x12[\n\nGetProduct\x12\".mavsdk.rpc.info.GetProductRequest\x1a#.mavsdk.rpc.info.GetProductResponse\"\x04\x80\xb5\x18\x01\x12[\n\nGetVersion\x12\".mavsdk.rpc.info.GetVersionRequest\x1a#.mavsdk.rpc.info.GetVersionResponse\"\x04\x80\xb5\x18\x01\x42\x1b\n\x0eio.mavsdk.infoB\tInfoProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])



_INFORESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.info.InfoResult.Result',
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
      name='RESULT_INFORMATION_NOT_RECEIVED_YET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1233,
  serialized_end=1322,
)
_sym_db.RegisterEnumDescriptor(_INFORESULT_RESULT)


_GETFLIGHTINFORMATIONREQUEST = _descriptor.Descriptor(
  name='GetFlightInformationRequest',
  full_name='mavsdk.rpc.info.GetFlightInformationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_end=87,
)


_GETFLIGHTINFORMATIONRESPONSE = _descriptor.Descriptor(
  name='GetFlightInformationResponse',
  full_name='mavsdk.rpc.info.GetFlightInformationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_result', full_name='mavsdk.rpc.info.GetFlightInformationResponse.info_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flight_info', full_name='mavsdk.rpc.info.GetFlightInformationResponse.flight_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=90,
  serialized_end=220,
)


_GETIDENTIFICATIONREQUEST = _descriptor.Descriptor(
  name='GetIdentificationRequest',
  full_name='mavsdk.rpc.info.GetIdentificationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=222,
  serialized_end=248,
)


_GETIDENTIFICATIONRESPONSE = _descriptor.Descriptor(
  name='GetIdentificationResponse',
  full_name='mavsdk.rpc.info.GetIdentificationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_result', full_name='mavsdk.rpc.info.GetIdentificationResponse.info_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identification', full_name='mavsdk.rpc.info.GetIdentificationResponse.identification', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=251,
  serialized_end=385,
)


_GETPRODUCTREQUEST = _descriptor.Descriptor(
  name='GetProductRequest',
  full_name='mavsdk.rpc.info.GetProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=387,
  serialized_end=406,
)


_GETPRODUCTRESPONSE = _descriptor.Descriptor(
  name='GetProductResponse',
  full_name='mavsdk.rpc.info.GetProductResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_result', full_name='mavsdk.rpc.info.GetProductResponse.info_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product', full_name='mavsdk.rpc.info.GetProductResponse.product', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=408,
  serialized_end=521,
)


_GETVERSIONREQUEST = _descriptor.Descriptor(
  name='GetVersionRequest',
  full_name='mavsdk.rpc.info.GetVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=523,
  serialized_end=542,
)


_GETVERSIONRESPONSE = _descriptor.Descriptor(
  name='GetVersionResponse',
  full_name='mavsdk.rpc.info.GetVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_result', full_name='mavsdk.rpc.info.GetVersionResponse.info_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='mavsdk.rpc.info.GetVersionResponse.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=544,
  serialized_end=657,
)


_FLIGHTINFO = _descriptor.Descriptor(
  name='FlightInfo',
  full_name='mavsdk.rpc.info.FlightInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_boot_ms', full_name='mavsdk.rpc.info.FlightInfo.time_boot_ms', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flight_uid', full_name='mavsdk.rpc.info.FlightInfo.flight_uid', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=659,
  serialized_end=713,
)


_IDENTIFICATION = _descriptor.Descriptor(
  name='Identification',
  full_name='mavsdk.rpc.info.Identification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hardware_uid', full_name='mavsdk.rpc.info.Identification.hardware_uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=715,
  serialized_end=753,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='mavsdk.rpc.info.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vendor_id', full_name='mavsdk.rpc.info.Product.vendor_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vendor_name', full_name='mavsdk.rpc.info.Product.vendor_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='mavsdk.rpc.info.Product.product_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_name', full_name='mavsdk.rpc.info.Product.product_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=755,
  serialized_end=846,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='mavsdk.rpc.info.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flight_sw_major', full_name='mavsdk.rpc.info.Version.flight_sw_major', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flight_sw_minor', full_name='mavsdk.rpc.info.Version.flight_sw_minor', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flight_sw_patch', full_name='mavsdk.rpc.info.Version.flight_sw_patch', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flight_sw_vendor_major', full_name='mavsdk.rpc.info.Version.flight_sw_vendor_major', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flight_sw_vendor_minor', full_name='mavsdk.rpc.info.Version.flight_sw_vendor_minor', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flight_sw_vendor_patch', full_name='mavsdk.rpc.info.Version.flight_sw_vendor_patch', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_sw_major', full_name='mavsdk.rpc.info.Version.os_sw_major', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_sw_minor', full_name='mavsdk.rpc.info.Version.os_sw_minor', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_sw_patch', full_name='mavsdk.rpc.info.Version.os_sw_patch', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flight_sw_git_hash', full_name='mavsdk.rpc.info.Version.flight_sw_git_hash', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_sw_git_hash', full_name='mavsdk.rpc.info.Version.os_sw_git_hash', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=849,
  serialized_end=1144,
)


_INFORESULT = _descriptor.Descriptor(
  name='InfoResult',
  full_name='mavsdk.rpc.info.InfoResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.info.InfoResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.info.InfoResult.result_str', index=1,
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
    _INFORESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1147,
  serialized_end=1322,
)

_GETFLIGHTINFORMATIONRESPONSE.fields_by_name['info_result'].message_type = _INFORESULT
_GETFLIGHTINFORMATIONRESPONSE.fields_by_name['flight_info'].message_type = _FLIGHTINFO
_GETIDENTIFICATIONRESPONSE.fields_by_name['info_result'].message_type = _INFORESULT
_GETIDENTIFICATIONRESPONSE.fields_by_name['identification'].message_type = _IDENTIFICATION
_GETPRODUCTRESPONSE.fields_by_name['info_result'].message_type = _INFORESULT
_GETPRODUCTRESPONSE.fields_by_name['product'].message_type = _PRODUCT
_GETVERSIONRESPONSE.fields_by_name['info_result'].message_type = _INFORESULT
_GETVERSIONRESPONSE.fields_by_name['version'].message_type = _VERSION
_INFORESULT.fields_by_name['result'].enum_type = _INFORESULT_RESULT
_INFORESULT_RESULT.containing_type = _INFORESULT
DESCRIPTOR.message_types_by_name['GetFlightInformationRequest'] = _GETFLIGHTINFORMATIONREQUEST
DESCRIPTOR.message_types_by_name['GetFlightInformationResponse'] = _GETFLIGHTINFORMATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetIdentificationRequest'] = _GETIDENTIFICATIONREQUEST
DESCRIPTOR.message_types_by_name['GetIdentificationResponse'] = _GETIDENTIFICATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetProductRequest'] = _GETPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['GetProductResponse'] = _GETPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['GetVersionRequest'] = _GETVERSIONREQUEST
DESCRIPTOR.message_types_by_name['GetVersionResponse'] = _GETVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['FlightInfo'] = _FLIGHTINFO
DESCRIPTOR.message_types_by_name['Identification'] = _IDENTIFICATION
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['InfoResult'] = _INFORESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFlightInformationRequest = _reflection.GeneratedProtocolMessageType('GetFlightInformationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFLIGHTINFORMATIONREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetFlightInformationRequest)
  })
_sym_db.RegisterMessage(GetFlightInformationRequest)

GetFlightInformationResponse = _reflection.GeneratedProtocolMessageType('GetFlightInformationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFLIGHTINFORMATIONRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetFlightInformationResponse)
  })
_sym_db.RegisterMessage(GetFlightInformationResponse)

GetIdentificationRequest = _reflection.GeneratedProtocolMessageType('GetIdentificationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIDENTIFICATIONREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetIdentificationRequest)
  })
_sym_db.RegisterMessage(GetIdentificationRequest)

GetIdentificationResponse = _reflection.GeneratedProtocolMessageType('GetIdentificationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETIDENTIFICATIONRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetIdentificationResponse)
  })
_sym_db.RegisterMessage(GetIdentificationResponse)

GetProductRequest = _reflection.GeneratedProtocolMessageType('GetProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetProductRequest)
  })
_sym_db.RegisterMessage(GetProductRequest)

GetProductResponse = _reflection.GeneratedProtocolMessageType('GetProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetProductResponse)
  })
_sym_db.RegisterMessage(GetProductResponse)

GetVersionRequest = _reflection.GeneratedProtocolMessageType('GetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONREQUEST,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetVersionRequest)
  })
_sym_db.RegisterMessage(GetVersionRequest)

GetVersionResponse = _reflection.GeneratedProtocolMessageType('GetVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONRESPONSE,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.GetVersionResponse)
  })
_sym_db.RegisterMessage(GetVersionResponse)

FlightInfo = _reflection.GeneratedProtocolMessageType('FlightInfo', (_message.Message,), {
  'DESCRIPTOR' : _FLIGHTINFO,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.FlightInfo)
  })
_sym_db.RegisterMessage(FlightInfo)

Identification = _reflection.GeneratedProtocolMessageType('Identification', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFICATION,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.Identification)
  })
_sym_db.RegisterMessage(Identification)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.Product)
  })
_sym_db.RegisterMessage(Product)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.Version)
  })
_sym_db.RegisterMessage(Version)

InfoResult = _reflection.GeneratedProtocolMessageType('InfoResult', (_message.Message,), {
  'DESCRIPTOR' : _INFORESULT,
  '__module__' : 'info.info_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.info.InfoResult)
  })
_sym_db.RegisterMessage(InfoResult)


DESCRIPTOR._options = None

_INFOSERVICE = _descriptor.ServiceDescriptor(
  name='InfoService',
  full_name='mavsdk.rpc.info.InfoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1325,
  serialized_end=1761,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFlightInformation',
    full_name='mavsdk.rpc.info.InfoService.GetFlightInformation',
    index=0,
    containing_service=None,
    input_type=_GETFLIGHTINFORMATIONREQUEST,
    output_type=_GETFLIGHTINFORMATIONRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetIdentification',
    full_name='mavsdk.rpc.info.InfoService.GetIdentification',
    index=1,
    containing_service=None,
    input_type=_GETIDENTIFICATIONREQUEST,
    output_type=_GETIDENTIFICATIONRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetProduct',
    full_name='mavsdk.rpc.info.InfoService.GetProduct',
    index=2,
    containing_service=None,
    input_type=_GETPRODUCTREQUEST,
    output_type=_GETPRODUCTRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVersion',
    full_name='mavsdk.rpc.info.InfoService.GetVersion',
    index=3,
    containing_service=None,
    input_type=_GETVERSIONREQUEST,
    output_type=_GETVERSIONRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INFOSERVICE)

DESCRIPTOR.services_by_name['InfoService'] = _INFOSERVICE

# @@protoc_insertion_point(module_scope)
