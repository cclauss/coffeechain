import logging

from sawtooth_sdk.processor.exceptions import InternalError
from sawtooth_sdk.processor.handler import TransactionHandler

from proto.config import TXF_NAME, ADDRESS_PREFIX, TXF_VERSIONS
from proto.coffee_pb2 import *
from proto import address


import logging

from sawtooth_sdk.processor.exceptions import InternalError
from sawtooth_sdk.processor.handler import TransactionHandler

from proto.config import TXF_NAME, ADDRESS_PREFIX, TXF_VERSIONS
from proto.coffee_pb2 import *
from proto import address


class StateManager(object):
   def __init__(self, context):
       self.context = context

   def get_and_parse(self, pb_class, addr):
       """
       Gets the data at the address and parses it into the `pb_class` type of object.
       Does not check that this is correct ;)  Make sure first that your addresses are right
       :param addr: The address of the state block to look up
       :param pb_class: The protofbuf class type to parse the data into
       """
       data = self.context.get_state([addr])[0]  # assume the address is correct
       obj = pb_class()
       obj.ParseFromString(data)
       return obj

   def set_for_object(self, pb_object):
       """
       Sets the state for a protobuf object based on the object type
       """
       class_name = type(pb_object).__name__
       addr = address.make_address(pb_object)  # generic address calc based on the class type
       content = pb_object.SerializeToString()

       print("setting state for %s [%s] => %r" % (class_name, addr, content))
       address_out = self.context.set_state({
           addr: content
       })
       if not address_out:
           raise InternalError("Error setting state for message %s" % class_name)


class ActualHandler(object):
   def __init__(self, context):
       self.state = StateManager(context)
       self.context = context

   def process(self, event_name, event_data):
       # better version of the apply from the real transaction handler
       handler = getattr(self, "handle_%s" % event_name, None)
       if handler:
           logging.info("calling '%s' with: %r" % handler.__name__, event_data)
           handler(event_data)
       else:
           raise InternalError("No handler for %s" % event_name)

   def handle_activate_code(self, event):
       code = self.state.get_and_parse(Code, address.for_code(event.message))
       code.activated_at = event.activated_at
       self.state.set_for_object(code)

   def handle_mint_code(self, event: Events.MintCode, context):
       assert isinstance(event, Events.MintCode)
       self.state.set_for_object(
           Code(message=event.message, company=event.company, created_at=event.created_at)
       )

   def handle_cert_create(self, event: Certification, context):
       assert isinstance(event, Certification)
       self.state.set_for_object(event)

   def handle_harvest_create(self, event: Harvest, context):
       assert isinstance(event, Harvest)
       self.state.set_for_object(event)


class CoffeeTransactionHandler(TransactionHandler):
   @property
   def family_name(self):
       return TXF_NAME

   @property
   def family_versions(self):
       return TXF_VERSIONS

   @property
   def namespaces(self):
       return [ADDRESS_PREFIX]

   def apply(self, transaction, context):
       logging.info("---- TRANSACTION RECIEVED ------------------------------------ ")
       evt = CoffeeChainEvents()
       evt.ParseFromString(transaction.payload)
       evt_name = evt.WhichOneof('payload')
       evt_data = getattr(evt, evt_name)
       ActualHandler(context).process(evt_name, evt_data)