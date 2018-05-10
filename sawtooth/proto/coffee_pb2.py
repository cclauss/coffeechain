# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/coffee.proto

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
  name='proto/coffee.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12proto/coffee.proto\"4\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ompany\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\"m\n\x04\x43ode\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x02 \x01(\x05\x12\x12\n\ncreated_at\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x63tivated_at\x18\x04 \x01(\t\x12\x19\n\x07product\x18\x05 \x01(\x0b\x32\x08.Product\"G\n\nHostedFile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08md5_hash\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x0b\n\x03url\x18\x04 \x01(\t\"\x98\x01\n\rCertification\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rcertifier_url\x18\x03 \x01(\t\x12\x14\n\x0cinstructions\x18\x04 \x01(\t\x12\x12\n\nvalid_from\x18\x05 \x01(\t\x12\x10\n\x08valid_to\x18\x06 \x01(\t\x12\x19\n\x04\x66ile\x18\x07 \x01(\x0b\x32\x0b.HostedFile\"g\n\x04\x46\x61rm\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x03(\t\x12\x1b\n\x08location\x18\x04 \x01(\x0b\x32\t.Location\x12\x16\n\x0e\x63\x65rtifications\x18\x05 \x03(\t\"9\n\x08Location\x12\x0b\n\x03lat\x18\x01 \x01(\x02\x12\x0b\n\x03lng\x18\x02 \x01(\x02\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"r\n\x07Harvest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04year\x18\x02 \x01(\x05\x12\r\n\x05month\x18\x03 \x01(\x05\x12\x1b\n\x08location\x18\x04 \x01(\x0b\x32\t.Location\x12\r\n\x05\x66\x61rms\x18\x05 \x03(\t\x12\x11\n\tshipments\x18\x06 \x03(\t\"\xae\x01\n\x08Shipment\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\n\n\x02kg\x18\x02 \x01(\x05\x12\x11\n\tship_name\x18\x03 \x01(\t\x12\x19\n\x06source\x18\x04 \x01(\x0b\x32\t.Location\x12\x1e\n\x0b\x64\x65stination\x18\x05 \x01(\x0b\x32\t.Location\x12\x12\n\nshipped_at\x18\x06 \x01(\t\x12\x13\n\x0brecieved_at\x18\x07 \x01(\t\x12\x12\n\nextra_info\x18\x08 \x03(\t\"W\n\x05Roast\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nroasted_at\x18\x02 \x01(\t\x12\x1b\n\x08location\x18\x03 \x01(\x0b\x32\t.Location\x12\x10\n\x08harvests\x18\x04 \x03(\t\"\xe4\x01\n\x06\x45vents\x1a@\n\x08MintCode\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x02 \x01(\x05\x12\x12\n\ncreated_at\x18\x03 \x01(\t\x1a\x35\n\x0c\x41\x63tivateCode\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63tivated_at\x18\x02 \x01(\t\x1a\x1a\n\x0b\x46\x61rmAddCert\x12\x0b\n\x03key\x18\x01 \x01(\t\x1a\x45\n\nAddRelated\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x12\n\nobject_key\x18\x02 \x01(\t\x12\x13\n\x0brelated_key\x18\x03 \x01(\t\"\xfc\x02\n\x11\x43offeeChainEvents\x12%\n\tmint_code\x18\x01 \x01(\x0b\x32\x10.Events.MintCodeH\x00\x12-\n\ractivate_code\x18\x02 \x01(\x0b\x32\x14.Events.ActivateCodeH\x00\x12%\n\x0b\x63\x65rt_create\x18\x03 \x01(\x0b\x32\x0e.CertificationH\x00\x12\"\n\x0eharvest_create\x18\x04 \x01(\x0b\x32\x08.HarvestH\x00\x12\x1c\n\x0b\x66\x61rm_create\x18\x05 \x01(\x0b\x32\x05.FarmH\x00\x12,\n\rfarm_add_cert\x18\x06 \x01(\x0b\x32\x13.Events.FarmAddCertH\x00\x12)\n\x0b\x61\x64\x64_related\x18\x07 \x01(\x0b\x32\x12.Events.AddRelatedH\x00\x12$\n\x0fshipment_create\x18\x08 \x01(\x0b\x32\t.ShipmentH\x00\x12\x1e\n\x0croast_create\x18\t \x01(\x0b\x32\x06.RoastH\x00\x42\t\n\x07payloadb\x06proto3')
)




_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Product.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company', full_name='Product.company', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Product.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=22,
  serialized_end=74,
)


_CODE = _descriptor.Descriptor(
  name='Code',
  full_name='Code',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Code.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company', full_name='Code.company', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='Code.created_at', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activated_at', full_name='Code.activated_at', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='Code.product', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=76,
  serialized_end=185,
)


_HOSTEDFILE = _descriptor.Descriptor(
  name='HostedFile',
  full_name='HostedFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HostedFile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='md5_hash', full_name='HostedFile.md5_hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='HostedFile.size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='HostedFile.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=187,
  serialized_end=258,
)


_CERTIFICATION = _descriptor.Descriptor(
  name='Certification',
  full_name='Certification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Certification.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Certification.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certifier_url', full_name='Certification.certifier_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instructions', full_name='Certification.instructions', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_from', full_name='Certification.valid_from', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_to', full_name='Certification.valid_to', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='Certification.file', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=261,
  serialized_end=413,
)


_FARM = _descriptor.Descriptor(
  name='Farm',
  full_name='Farm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Farm.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Farm.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='Farm.address', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='Farm.location', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certifications', full_name='Farm.certifications', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=415,
  serialized_end=518,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='Location.lat', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lng', full_name='Location.lng', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Location.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=520,
  serialized_end=577,
)


_HARVEST = _descriptor.Descriptor(
  name='Harvest',
  full_name='Harvest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Harvest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='Harvest.year', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='Harvest.month', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='Harvest.location', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='farms', full_name='Harvest.farms', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipments', full_name='Harvest.shipments', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=579,
  serialized_end=693,
)


_SHIPMENT = _descriptor.Descriptor(
  name='Shipment',
  full_name='Shipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Shipment.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kg', full_name='Shipment.kg', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ship_name', full_name='Shipment.ship_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='Shipment.source', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='Shipment.destination', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipped_at', full_name='Shipment.shipped_at', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recieved_at', full_name='Shipment.recieved_at', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_info', full_name='Shipment.extra_info', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=696,
  serialized_end=870,
)


_ROAST = _descriptor.Descriptor(
  name='Roast',
  full_name='Roast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Roast.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roasted_at', full_name='Roast.roasted_at', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='Roast.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='harvests', full_name='Roast.harvests', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=872,
  serialized_end=959,
)


_EVENTS_MINTCODE = _descriptor.Descriptor(
  name='MintCode',
  full_name='Events.MintCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Events.MintCode.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company', full_name='Events.MintCode.company', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='Events.MintCode.created_at', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=972,
  serialized_end=1036,
)

_EVENTS_ACTIVATECODE = _descriptor.Descriptor(
  name='ActivateCode',
  full_name='Events.ActivateCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Events.ActivateCode.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activated_at', full_name='Events.ActivateCode.activated_at', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1038,
  serialized_end=1091,
)

_EVENTS_FARMADDCERT = _descriptor.Descriptor(
  name='FarmAddCert',
  full_name='Events.FarmAddCert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Events.FarmAddCert.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1093,
  serialized_end=1119,
)

_EVENTS_ADDRELATED = _descriptor.Descriptor(
  name='AddRelated',
  full_name='Events.AddRelated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='Events.AddRelated.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_key', full_name='Events.AddRelated.object_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='related_key', full_name='Events.AddRelated.related_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1121,
  serialized_end=1190,
)

_EVENTS = _descriptor.Descriptor(
  name='Events',
  full_name='Events',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_EVENTS_MINTCODE, _EVENTS_ACTIVATECODE, _EVENTS_FARMADDCERT, _EVENTS_ADDRELATED, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=962,
  serialized_end=1190,
)


_COFFEECHAINEVENTS = _descriptor.Descriptor(
  name='CoffeeChainEvents',
  full_name='CoffeeChainEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mint_code', full_name='CoffeeChainEvents.mint_code', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activate_code', full_name='CoffeeChainEvents.activate_code', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cert_create', full_name='CoffeeChainEvents.cert_create', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='harvest_create', full_name='CoffeeChainEvents.harvest_create', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='farm_create', full_name='CoffeeChainEvents.farm_create', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='farm_add_cert', full_name='CoffeeChainEvents.farm_add_cert', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_related', full_name='CoffeeChainEvents.add_related', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shipment_create', full_name='CoffeeChainEvents.shipment_create', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roast_create', full_name='CoffeeChainEvents.roast_create', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='CoffeeChainEvents.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1193,
  serialized_end=1573,
)

_CODE.fields_by_name['product'].message_type = _PRODUCT
_CERTIFICATION.fields_by_name['file'].message_type = _HOSTEDFILE
_FARM.fields_by_name['location'].message_type = _LOCATION
_HARVEST.fields_by_name['location'].message_type = _LOCATION
_SHIPMENT.fields_by_name['source'].message_type = _LOCATION
_SHIPMENT.fields_by_name['destination'].message_type = _LOCATION
_ROAST.fields_by_name['location'].message_type = _LOCATION
_EVENTS_MINTCODE.containing_type = _EVENTS
_EVENTS_ACTIVATECODE.containing_type = _EVENTS
_EVENTS_FARMADDCERT.containing_type = _EVENTS
_EVENTS_ADDRELATED.containing_type = _EVENTS
_COFFEECHAINEVENTS.fields_by_name['mint_code'].message_type = _EVENTS_MINTCODE
_COFFEECHAINEVENTS.fields_by_name['activate_code'].message_type = _EVENTS_ACTIVATECODE
_COFFEECHAINEVENTS.fields_by_name['cert_create'].message_type = _CERTIFICATION
_COFFEECHAINEVENTS.fields_by_name['harvest_create'].message_type = _HARVEST
_COFFEECHAINEVENTS.fields_by_name['farm_create'].message_type = _FARM
_COFFEECHAINEVENTS.fields_by_name['farm_add_cert'].message_type = _EVENTS_FARMADDCERT
_COFFEECHAINEVENTS.fields_by_name['add_related'].message_type = _EVENTS_ADDRELATED
_COFFEECHAINEVENTS.fields_by_name['shipment_create'].message_type = _SHIPMENT
_COFFEECHAINEVENTS.fields_by_name['roast_create'].message_type = _ROAST
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['mint_code'])
_COFFEECHAINEVENTS.fields_by_name['mint_code'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['activate_code'])
_COFFEECHAINEVENTS.fields_by_name['activate_code'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['cert_create'])
_COFFEECHAINEVENTS.fields_by_name['cert_create'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['harvest_create'])
_COFFEECHAINEVENTS.fields_by_name['harvest_create'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['farm_create'])
_COFFEECHAINEVENTS.fields_by_name['farm_create'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['farm_add_cert'])
_COFFEECHAINEVENTS.fields_by_name['farm_add_cert'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['add_related'])
_COFFEECHAINEVENTS.fields_by_name['add_related'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['shipment_create'])
_COFFEECHAINEVENTS.fields_by_name['shipment_create'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
_COFFEECHAINEVENTS.oneofs_by_name['payload'].fields.append(
  _COFFEECHAINEVENTS.fields_by_name['roast_create'])
_COFFEECHAINEVENTS.fields_by_name['roast_create'].containing_oneof = _COFFEECHAINEVENTS.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Code'] = _CODE
DESCRIPTOR.message_types_by_name['HostedFile'] = _HOSTEDFILE
DESCRIPTOR.message_types_by_name['Certification'] = _CERTIFICATION
DESCRIPTOR.message_types_by_name['Farm'] = _FARM
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Harvest'] = _HARVEST
DESCRIPTOR.message_types_by_name['Shipment'] = _SHIPMENT
DESCRIPTOR.message_types_by_name['Roast'] = _ROAST
DESCRIPTOR.message_types_by_name['Events'] = _EVENTS
DESCRIPTOR.message_types_by_name['CoffeeChainEvents'] = _COFFEECHAINEVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Product)
  ))
_sym_db.RegisterMessage(Product)

Code = _reflection.GeneratedProtocolMessageType('Code', (_message.Message,), dict(
  DESCRIPTOR = _CODE,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Code)
  ))
_sym_db.RegisterMessage(Code)

HostedFile = _reflection.GeneratedProtocolMessageType('HostedFile', (_message.Message,), dict(
  DESCRIPTOR = _HOSTEDFILE,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:HostedFile)
  ))
_sym_db.RegisterMessage(HostedFile)

Certification = _reflection.GeneratedProtocolMessageType('Certification', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATION,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Certification)
  ))
_sym_db.RegisterMessage(Certification)

Farm = _reflection.GeneratedProtocolMessageType('Farm', (_message.Message,), dict(
  DESCRIPTOR = _FARM,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Farm)
  ))
_sym_db.RegisterMessage(Farm)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  ))
_sym_db.RegisterMessage(Location)

Harvest = _reflection.GeneratedProtocolMessageType('Harvest', (_message.Message,), dict(
  DESCRIPTOR = _HARVEST,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Harvest)
  ))
_sym_db.RegisterMessage(Harvest)

Shipment = _reflection.GeneratedProtocolMessageType('Shipment', (_message.Message,), dict(
  DESCRIPTOR = _SHIPMENT,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Shipment)
  ))
_sym_db.RegisterMessage(Shipment)

Roast = _reflection.GeneratedProtocolMessageType('Roast', (_message.Message,), dict(
  DESCRIPTOR = _ROAST,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Roast)
  ))
_sym_db.RegisterMessage(Roast)

Events = _reflection.GeneratedProtocolMessageType('Events', (_message.Message,), dict(

  MintCode = _reflection.GeneratedProtocolMessageType('MintCode', (_message.Message,), dict(
    DESCRIPTOR = _EVENTS_MINTCODE,
    __module__ = 'proto.coffee_pb2'
    # @@protoc_insertion_point(class_scope:Events.MintCode)
    ))
  ,

  ActivateCode = _reflection.GeneratedProtocolMessageType('ActivateCode', (_message.Message,), dict(
    DESCRIPTOR = _EVENTS_ACTIVATECODE,
    __module__ = 'proto.coffee_pb2'
    # @@protoc_insertion_point(class_scope:Events.ActivateCode)
    ))
  ,

  FarmAddCert = _reflection.GeneratedProtocolMessageType('FarmAddCert', (_message.Message,), dict(
    DESCRIPTOR = _EVENTS_FARMADDCERT,
    __module__ = 'proto.coffee_pb2'
    # @@protoc_insertion_point(class_scope:Events.FarmAddCert)
    ))
  ,

  AddRelated = _reflection.GeneratedProtocolMessageType('AddRelated', (_message.Message,), dict(
    DESCRIPTOR = _EVENTS_ADDRELATED,
    __module__ = 'proto.coffee_pb2'
    # @@protoc_insertion_point(class_scope:Events.AddRelated)
    ))
  ,
  DESCRIPTOR = _EVENTS,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:Events)
  ))
_sym_db.RegisterMessage(Events)
_sym_db.RegisterMessage(Events.MintCode)
_sym_db.RegisterMessage(Events.ActivateCode)
_sym_db.RegisterMessage(Events.FarmAddCert)
_sym_db.RegisterMessage(Events.AddRelated)

CoffeeChainEvents = _reflection.GeneratedProtocolMessageType('CoffeeChainEvents', (_message.Message,), dict(
  DESCRIPTOR = _COFFEECHAINEVENTS,
  __module__ = 'proto.coffee_pb2'
  # @@protoc_insertion_point(class_scope:CoffeeChainEvents)
  ))
_sym_db.RegisterMessage(CoffeeChainEvents)


# @@protoc_insertion_point(module_scope)
