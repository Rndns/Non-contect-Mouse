# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imagePrep.proto

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
  name='imagePrep.proto',
  package='imagePrep',
  syntax='proto3',
  serialized_pb=_b('\n\x0fimagePrep.proto\x12\timagePrep\"\x19\n\x05Image\x12\x10\n\x08gPicture\x18\x01 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='imagePrep.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gPicture', full_name='imagePrep.Image.gPicture', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=30,
  serialized_end=55,
)

DESCRIPTOR.message_types_by_name['Image'] = _IMAGE

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'imagePrep_pb2'
  # @@protoc_insertion_point(class_scope:imagePrep.Image)
  ))
_sym_db.RegisterMessage(Image)


# @@protoc_insertion_point(module_scope)
