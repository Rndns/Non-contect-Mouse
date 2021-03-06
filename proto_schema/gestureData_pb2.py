# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gestureData.proto

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
  name='gestureData.proto',
  package='gesetureData',
  syntax='proto3',
  serialized_pb=_b('\n\x11gestureData.proto\x12\x0cgesetureData\",\n\x0cPointHistory\x12\r\n\x05X_loc\x18\x01 \x01(\x05\x12\r\n\x05Y_loc\x18\x02 \x01(\x05\"!\n\tLandmarks\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\xcc\x04\n\x04\x44\x61ta\x12*\n\x05hsign\x18\x01 \x01(\x0e\x32\x1b.gesetureData.Data.HandSign\x12,\n\x05\x66sign\x18\x02 \x01(\x0e\x32\x1d.gesetureData.Data.FingerSign\x12)\n\x05point\x18\x03 \x03(\x0b\x32\x1a.gesetureData.PointHistory\x12/\n\tmouseMode\x18\x04 \x01(\x0e\x32\x1c.gesetureData.Data.MouseMode\x12%\n\x04mark\x18\x05 \x03(\x0b\x32\x17.gesetureData.Landmarks\"I\n\x08HandSign\x12\x11\n\rHandSign_open\x10\x00\x12\x12\n\x0eHandSign_close\x10\x01\x12\x16\n\x12HandSign_oneFinger\x10\x02\"s\n\nFingerSign\x12\x13\n\x0f\x46ingerSign_stop\x10\x00\x12\x18\n\x14\x46ingerSign_clockwise\x10\x01\x12\x1f\n\x1b\x46ingerSign_counterClockwise\x10\x02\x12\x15\n\x11\x46ingerSign_moving\x10\x03\"\xa6\x01\n\tMouseMode\x12\x16\n\x12MouseMode_eNothing\x10\x00\x12\x19\n\x15MouseMode_ePageScroll\x10\x01\x12\x14\n\x10MouseMode_eClick\x10\x02\x12\x1a\n\x16MouseMode_eForwardPage\x10\x03\x12\x17\n\x13MouseMode_eBackPage\x10\x04\x12\x1b\n\x17MouseMode_eMouseControl\x10\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DATA_HANDSIGN = _descriptor.EnumDescriptor(
  name='HandSign',
  full_name='gesetureData.Data.HandSign',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HandSign_open', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HandSign_close', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HandSign_oneFinger', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=346,
  serialized_end=419,
)
_sym_db.RegisterEnumDescriptor(_DATA_HANDSIGN)

_DATA_FINGERSIGN = _descriptor.EnumDescriptor(
  name='FingerSign',
  full_name='gesetureData.Data.FingerSign',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FingerSign_stop', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FingerSign_clockwise', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FingerSign_counterClockwise', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FingerSign_moving', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=421,
  serialized_end=536,
)
_sym_db.RegisterEnumDescriptor(_DATA_FINGERSIGN)

_DATA_MOUSEMODE = _descriptor.EnumDescriptor(
  name='MouseMode',
  full_name='gesetureData.Data.MouseMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MouseMode_eNothing', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MouseMode_ePageScroll', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MouseMode_eClick', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MouseMode_eForwardPage', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MouseMode_eBackPage', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MouseMode_eMouseControl', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=539,
  serialized_end=705,
)
_sym_db.RegisterEnumDescriptor(_DATA_MOUSEMODE)


_POINTHISTORY = _descriptor.Descriptor(
  name='PointHistory',
  full_name='gesetureData.PointHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='X_loc', full_name='gesetureData.PointHistory.X_loc', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Y_loc', full_name='gesetureData.PointHistory.Y_loc', index=1,
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
  serialized_start=35,
  serialized_end=79,
)


_LANDMARKS = _descriptor.Descriptor(
  name='Landmarks',
  full_name='gesetureData.Landmarks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='gesetureData.Landmarks.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='gesetureData.Landmarks.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=81,
  serialized_end=114,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='gesetureData.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hsign', full_name='gesetureData.Data.hsign', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fsign', full_name='gesetureData.Data.fsign', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='gesetureData.Data.point', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mouseMode', full_name='gesetureData.Data.mouseMode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mark', full_name='gesetureData.Data.mark', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATA_HANDSIGN,
    _DATA_FINGERSIGN,
    _DATA_MOUSEMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=705,
)

_DATA.fields_by_name['hsign'].enum_type = _DATA_HANDSIGN
_DATA.fields_by_name['fsign'].enum_type = _DATA_FINGERSIGN
_DATA.fields_by_name['point'].message_type = _POINTHISTORY
_DATA.fields_by_name['mouseMode'].enum_type = _DATA_MOUSEMODE
_DATA.fields_by_name['mark'].message_type = _LANDMARKS
_DATA_HANDSIGN.containing_type = _DATA
_DATA_FINGERSIGN.containing_type = _DATA
_DATA_MOUSEMODE.containing_type = _DATA
DESCRIPTOR.message_types_by_name['PointHistory'] = _POINTHISTORY
DESCRIPTOR.message_types_by_name['Landmarks'] = _LANDMARKS
DESCRIPTOR.message_types_by_name['Data'] = _DATA

PointHistory = _reflection.GeneratedProtocolMessageType('PointHistory', (_message.Message,), dict(
  DESCRIPTOR = _POINTHISTORY,
  __module__ = 'gestureData_pb2'
  # @@protoc_insertion_point(class_scope:gesetureData.PointHistory)
  ))
_sym_db.RegisterMessage(PointHistory)

Landmarks = _reflection.GeneratedProtocolMessageType('Landmarks', (_message.Message,), dict(
  DESCRIPTOR = _LANDMARKS,
  __module__ = 'gestureData_pb2'
  # @@protoc_insertion_point(class_scope:gesetureData.Landmarks)
  ))
_sym_db.RegisterMessage(Landmarks)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'gestureData_pb2'
  # @@protoc_insertion_point(class_scope:gesetureData.Data)
  ))
_sym_db.RegisterMessage(Data)


# @@protoc_insertion_point(module_scope)
