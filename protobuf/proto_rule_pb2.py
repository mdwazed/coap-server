# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_rule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_rule.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10proto_rule.proto\"m\n\tProtoRule\x12\x14\n\x0c\x63hannel_mask\x18\x01 \x01(\r\x12\x1d\n\tcondition\x18\x02 \x01(\x0e\x32\n.Condition\x12\x12\n\nparameters\x18\x03 \x03(\x11\x12\x17\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32\x07.Action*\xba\x01\n\tCondition\x12\x19\n\x15\x43ONDITION_UNSPECIFIED\x10\x00\x12\x16\n\x12\x43ONDITION_DISABLED\x10\x01\x12\x1c\n\x18\x43ONDITION_HIGH_THRESHOLD\x10\x02\x12\x1b\n\x17\x43ONDITION_LOW_THRESHOLD\x10\x03\x12\x1c\n\x18\x43ONDITION_DIFF_THRESHOLD\x10\x04\x12!\n\x1d\x43ONDITION_BINARY_CHANGE_STATE\x10\x05*A\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x41\x43TION_TRIGGER_TRANSMISSION\x10\x01\x62\x06proto3'
)

_CONDITION = _descriptor.EnumDescriptor(
  name='Condition',
  full_name='Condition',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONDITION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONDITION_DISABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONDITION_HIGH_THRESHOLD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONDITION_LOW_THRESHOLD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONDITION_DIFF_THRESHOLD', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONDITION_BINARY_CHANGE_STATE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=132,
  serialized_end=318,
)
_sym_db.RegisterEnumDescriptor(_CONDITION)

Condition = enum_type_wrapper.EnumTypeWrapper(_CONDITION)
_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_TRIGGER_TRANSMISSION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=320,
  serialized_end=385,
)
_sym_db.RegisterEnumDescriptor(_ACTION)

Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
CONDITION_UNSPECIFIED = 0
CONDITION_DISABLED = 1
CONDITION_HIGH_THRESHOLD = 2
CONDITION_LOW_THRESHOLD = 3
CONDITION_DIFF_THRESHOLD = 4
CONDITION_BINARY_CHANGE_STATE = 5
ACTION_UNSPECIFIED = 0
ACTION_TRIGGER_TRANSMISSION = 1



_PROTORULE = _descriptor.Descriptor(
  name='ProtoRule',
  full_name='ProtoRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_mask', full_name='ProtoRule.channel_mask', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='condition', full_name='ProtoRule.condition', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='ProtoRule.parameters', index=2,
      number=3, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='ProtoRule.action', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=20,
  serialized_end=129,
)

_PROTORULE.fields_by_name['condition'].enum_type = _CONDITION
_PROTORULE.fields_by_name['action'].enum_type = _ACTION
DESCRIPTOR.message_types_by_name['ProtoRule'] = _PROTORULE
DESCRIPTOR.enum_types_by_name['Condition'] = _CONDITION
DESCRIPTOR.enum_types_by_name['Action'] = _ACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtoRule = _reflection.GeneratedProtocolMessageType('ProtoRule', (_message.Message,), {
  'DESCRIPTOR' : _PROTORULE,
  '__module__' : 'proto_rule_pb2'
  # @@protoc_insertion_point(class_scope:ProtoRule)
  })
_sym_db.RegisterMessage(ProtoRule)


# @@protoc_insertion_point(module_scope)