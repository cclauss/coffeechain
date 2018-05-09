import logging

from proto import address
from proto.coffee_pb2 import *
from proto.config import TXF_NAME, ADDRESS_PREFIX, TXF_VERSIONS

from google.protobuf.message import DecodeError

from sawtooth_sdk.processor.exceptions import InternalError, InvalidTransaction
from sawtooth_sdk.processor.handler import TransactionHandler


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
            logging.info("calling '%s' with: %r" % (handler.__name__, event_data))
            handler(event_data)
        else:
            raise InternalError("No handler for %s" % event_name)

    def handle_activate_code(self, event):
        code = self.state.get_and_parse(Code, address.for_code(event.message))
        code.activated_at = event.activated_at
        self.state.set_for_object(code)

    def handle_mint_code(self, event: Events.MintCode):
        assert isinstance(event, Events.MintCode)
        self.state.set_for_object(
            Code(message=event.message, company=event.company, created_at=event.created_at)
        )

    def handle_cert_create(self, event: Certification):
        assert isinstance(event, Certification)
        self.state.set_for_object(event)

    def handle_harvest_create(self, event: Harvest):
        assert isinstance(event, Harvest)
        self.state.set_for_object(event)

    def handle_farm_create(self, event):
        assert isinstance(event, Farm)
        self.state.set_for_object(event)

    def handle_add_related(self, event):
        assert isinstance(event, Events.AddRelated)

        def add(event, related_class, src_class, list_name):
            src = self.state.get_and_parse(src_class, address.for_harvest(event.object_key))
            related = self.state.get_and_parse(related_class, address.for_farm(event.related_key))
            getattr(src, list_name).append(related.key)
            self.state.set_for_object(src)

        action_map = {
            "harvest_farm": (Harvest, Farm, "farms"),
            "harvest_shipment": (Harvest, Shipment, "shipments")
        }

        if event.action not in action_map:
            raise InvalidTransaction("Unmapped action for AddRelated")

        add(event, *action_map[event.action])


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
        try:
            evt.ParseFromString(transaction.payload)
        except DecodeError as e:
            print("Error decoding message %s" % e)
            print("    body: %r" % transaction.payload)
            return

        evt_name = evt.WhichOneof('payload')
        evt_data = getattr(evt, evt_name)
        ActualHandler(context).process(evt_name, evt_data)
