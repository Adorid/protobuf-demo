# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='demo',
  syntax='proto3',
  serialized_pb=_b('\n\rservice.proto\x12\x04\x64\x65mo\"/\n\x11GetWeatherRequest\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ys\x18\x02 \x01(\x05\"|\n\x0bWeatherInfo\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x17\n\x0ftemperature_low\x18\x03 \x01(\x05\x12\x18\n\x10temperature_high\x18\x04 \x01(\x05\x12\x0c\n\x04wind\x18\x05 \x01(\x05\x12\x10\n\x08humidity\x18\x06 \x01(\x05\"<\n\x12GetWeatherResponse\x12&\n\x0bweatherinfo\x18\x01 \x03(\x0b\x32\x11.demo.WeatherInfob\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETWEATHERREQUEST = _descriptor.Descriptor(
  name='GetWeatherRequest',
  full_name='demo.GetWeatherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='demo.GetWeatherRequest.city', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='days', full_name='demo.GetWeatherRequest.days', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=70,
)


_WEATHERINFO = _descriptor.Descriptor(
  name='WeatherInfo',
  full_name='demo.WeatherInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='demo.WeatherInfo.city', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='demo.WeatherInfo.date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_low', full_name='demo.WeatherInfo.temperature_low', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_high', full_name='demo.WeatherInfo.temperature_high', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wind', full_name='demo.WeatherInfo.wind', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='humidity', full_name='demo.WeatherInfo.humidity', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=196,
)


_GETWEATHERRESPONSE = _descriptor.Descriptor(
  name='GetWeatherResponse',
  full_name='demo.GetWeatherResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weatherinfo', full_name='demo.GetWeatherResponse.weatherinfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=258,
)

_GETWEATHERRESPONSE.fields_by_name['weatherinfo'].message_type = _WEATHERINFO
DESCRIPTOR.message_types_by_name['GetWeatherRequest'] = _GETWEATHERREQUEST
DESCRIPTOR.message_types_by_name['WeatherInfo'] = _WEATHERINFO
DESCRIPTOR.message_types_by_name['GetWeatherResponse'] = _GETWEATHERRESPONSE

GetWeatherRequest = _reflection.GeneratedProtocolMessageType('GetWeatherRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETWEATHERREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:demo.GetWeatherRequest)
  ))
_sym_db.RegisterMessage(GetWeatherRequest)

WeatherInfo = _reflection.GeneratedProtocolMessageType('WeatherInfo', (_message.Message,), dict(
  DESCRIPTOR = _WEATHERINFO,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:demo.WeatherInfo)
  ))
_sym_db.RegisterMessage(WeatherInfo)

GetWeatherResponse = _reflection.GeneratedProtocolMessageType('GetWeatherResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETWEATHERRESPONSE,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:demo.GetWeatherResponse)
  ))
_sym_db.RegisterMessage(GetWeatherResponse)


# @@protoc_insertion_point(module_scope)
