# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_minder2_murmur/main.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grpc_minder2_murmur import murmur_pb2 as grpc__minder2__murmur_dot_murmur__pb2
from grpc_minder2_murmur import database_pb2 as grpc__minder2__murmur_dot_database__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_minder2_murmur/main.proto',
  package='grpc_minder2_murmur',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1egrpc_minder2_murmur/main.proto\x12\x13grpc_minder2_murmur\x1a grpc_minder2_murmur/murmur.proto\x1a\"grpc_minder2_murmur/database.proto\"\x06\n\x04Void2\x99\x02\n\rMurmurService\x12P\n\x06\x43reate\x12+.grpc_minder2_murmur.murmur.MurmurContainer\x1a\x19.grpc_minder2_murmur.Void\x12P\n\x07\x44\x65stroy\x12*.grpc_minder2_murmur.murmur.DestroyRequest\x1a\x19.grpc_minder2_murmur.Void\x12\x64\n\x08GetImage\x12+.grpc_minder2_murmur.murmur.MurmurContainer\x1a+.grpc_minder2_murmur.murmur.MurmurContainer2\xbb\x01\n\x0f\x44\x61tabaseService\x12T\n\x06\x43reate\x12/.grpc_minder2_murmur.database.DatabaseContainer\x1a\x19.grpc_minder2_murmur.Void\x12R\n\x07\x44\x65stroy\x12,.grpc_minder2_murmur.database.DestroyRequest\x1a\x19.grpc_minder2_murmur.Voidb\x06proto3')
  ,
  dependencies=[grpc__minder2__murmur_dot_murmur__pb2.DESCRIPTOR,grpc__minder2__murmur_dot_database__pb2.DESCRIPTOR,])




_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='grpc_minder2_murmur.Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=125,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['Void'] = _VOID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), dict(
  DESCRIPTOR = _VOID,
  __module__ = 'grpc_minder2_murmur.main_pb2'
  # @@protoc_insertion_point(class_scope:grpc_minder2_murmur.Void)
  ))
_sym_db.RegisterMessage(Void)



_MURMURSERVICE = _descriptor.ServiceDescriptor(
  name='MurmurService',
  full_name='grpc_minder2_murmur.MurmurService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=134,
  serialized_end=415,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='grpc_minder2_murmur.MurmurService.Create',
    index=0,
    containing_service=None,
    input_type=grpc__minder2__murmur_dot_murmur__pb2._MURMURCONTAINER,
    output_type=_VOID,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='grpc_minder2_murmur.MurmurService.Destroy',
    index=1,
    containing_service=None,
    input_type=grpc__minder2__murmur_dot_murmur__pb2._DESTROYREQUEST,
    output_type=_VOID,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetImage',
    full_name='grpc_minder2_murmur.MurmurService.GetImage',
    index=2,
    containing_service=None,
    input_type=grpc__minder2__murmur_dot_murmur__pb2._MURMURCONTAINER,
    output_type=grpc__minder2__murmur_dot_murmur__pb2._MURMURCONTAINER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MURMURSERVICE)

DESCRIPTOR.services_by_name['MurmurService'] = _MURMURSERVICE


_DATABASESERVICE = _descriptor.ServiceDescriptor(
  name='DatabaseService',
  full_name='grpc_minder2_murmur.DatabaseService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=418,
  serialized_end=605,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='grpc_minder2_murmur.DatabaseService.Create',
    index=0,
    containing_service=None,
    input_type=grpc__minder2__murmur_dot_database__pb2._DATABASECONTAINER,
    output_type=_VOID,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='grpc_minder2_murmur.DatabaseService.Destroy',
    index=1,
    containing_service=None,
    input_type=grpc__minder2__murmur_dot_database__pb2._DESTROYREQUEST,
    output_type=_VOID,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATABASESERVICE)

DESCRIPTOR.services_by_name['DatabaseService'] = _DATABASESERVICE

# @@protoc_insertion_point(module_scope)