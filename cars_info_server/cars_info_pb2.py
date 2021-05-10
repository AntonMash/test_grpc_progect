# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cars_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cars_info.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63\x61rs_info.proto\"%\n\x12RequestForOneModel\x12\x0f\n\x07modelId\x18\x01 \x01(\x05\"\"\n\x0fRequestForBrand\x12\x0f\n\x07\x62randId\x18\x01 \x01(\x05\"L\n\x0fInfoForOneModel\x12\r\n\x05\x62rand\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\r\n\x05price\x18\x04 \x01(\x02\"Q\n\x14ResponseInfoForBrand\x12\r\n\x05\x62rand\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0c\n\x04year\x18\x03 \x01(\x05\x12\r\n\x05price\x18\x04 \x01(\x02\"5\n\x13ResponseForOneModel\x12\x1e\n\x04info\x18\x01 \x03(\x0b\x32\x10.InfoForOneModel2\x86\x01\n\x04Info\x12>\n\x0fGetInfoForModel\x12\x13.RequestForOneModel\x1a\x14.ResponseForOneModel\"\x00\x12>\n\x0fGetInfoForBrand\x12\x10.RequestForBrand\x1a\x15.ResponseInfoForBrand\"\x00\x30\x01\x62\x06proto3'
)




_REQUESTFORONEMODEL = _descriptor.Descriptor(
  name='RequestForOneModel',
  full_name='RequestForOneModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='modelId', full_name='RequestForOneModel.modelId', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=19,
  serialized_end=56,
)


_REQUESTFORBRAND = _descriptor.Descriptor(
  name='RequestForBrand',
  full_name='RequestForBrand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='brandId', full_name='RequestForBrand.brandId', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=58,
  serialized_end=92,
)


_INFOFORONEMODEL = _descriptor.Descriptor(
  name='InfoForOneModel',
  full_name='InfoForOneModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='brand', full_name='InfoForOneModel.brand', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model', full_name='InfoForOneModel.model', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='InfoForOneModel.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='InfoForOneModel.price', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=94,
  serialized_end=170,
)


_RESPONSEINFOFORBRAND = _descriptor.Descriptor(
  name='ResponseInfoForBrand',
  full_name='ResponseInfoForBrand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='brand', full_name='ResponseInfoForBrand.brand', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model', full_name='ResponseInfoForBrand.model', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='ResponseInfoForBrand.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='ResponseInfoForBrand.price', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=172,
  serialized_end=253,
)


_RESPONSEFORONEMODEL = _descriptor.Descriptor(
  name='ResponseForOneModel',
  full_name='ResponseForOneModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='ResponseForOneModel.info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=255,
  serialized_end=308,
)

_RESPONSEFORONEMODEL.fields_by_name['info'].message_type = _INFOFORONEMODEL
DESCRIPTOR.message_types_by_name['RequestForOneModel'] = _REQUESTFORONEMODEL
DESCRIPTOR.message_types_by_name['RequestForBrand'] = _REQUESTFORBRAND
DESCRIPTOR.message_types_by_name['InfoForOneModel'] = _INFOFORONEMODEL
DESCRIPTOR.message_types_by_name['ResponseInfoForBrand'] = _RESPONSEINFOFORBRAND
DESCRIPTOR.message_types_by_name['ResponseForOneModel'] = _RESPONSEFORONEMODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestForOneModel = _reflection.GeneratedProtocolMessageType('RequestForOneModel', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTFORONEMODEL,
  '__module__' : 'cars_info_pb2'
  # @@protoc_insertion_point(class_scope:RequestForOneModel)
  })
_sym_db.RegisterMessage(RequestForOneModel)

RequestForBrand = _reflection.GeneratedProtocolMessageType('RequestForBrand', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTFORBRAND,
  '__module__' : 'cars_info_pb2'
  # @@protoc_insertion_point(class_scope:RequestForBrand)
  })
_sym_db.RegisterMessage(RequestForBrand)

InfoForOneModel = _reflection.GeneratedProtocolMessageType('InfoForOneModel', (_message.Message,), {
  'DESCRIPTOR' : _INFOFORONEMODEL,
  '__module__' : 'cars_info_pb2'
  # @@protoc_insertion_point(class_scope:InfoForOneModel)
  })
_sym_db.RegisterMessage(InfoForOneModel)

ResponseInfoForBrand = _reflection.GeneratedProtocolMessageType('ResponseInfoForBrand', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEINFOFORBRAND,
  '__module__' : 'cars_info_pb2'
  # @@protoc_insertion_point(class_scope:ResponseInfoForBrand)
  })
_sym_db.RegisterMessage(ResponseInfoForBrand)

ResponseForOneModel = _reflection.GeneratedProtocolMessageType('ResponseForOneModel', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEFORONEMODEL,
  '__module__' : 'cars_info_pb2'
  # @@protoc_insertion_point(class_scope:ResponseForOneModel)
  })
_sym_db.RegisterMessage(ResponseForOneModel)



_INFO = _descriptor.ServiceDescriptor(
  name='Info',
  full_name='Info',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=311,
  serialized_end=445,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetInfoForModel',
    full_name='Info.GetInfoForModel',
    index=0,
    containing_service=None,
    input_type=_REQUESTFORONEMODEL,
    output_type=_RESPONSEFORONEMODEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetInfoForBrand',
    full_name='Info.GetInfoForBrand',
    index=1,
    containing_service=None,
    input_type=_REQUESTFORBRAND,
    output_type=_RESPONSEINFOFORBRAND,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INFO)

DESCRIPTOR.services_by_name['Info'] = _INFO

# @@protoc_insertion_point(module_scope)