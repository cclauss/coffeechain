import logging

from google.protobuf.message import DecodeError
from proto.coffee_pb2 import *
from proto.config import TXF_NAME, ADDRESS_PREFIX, TXF_VERSIONS
from sawtooth_sdk.processor.exceptions import InternalError
from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.protobuf.state_context_pb2 import TpStateEntry

from proto import address

logger = logging.getLogger(__name__)


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

        # assume the address is correct
        data = self.context.get_state([addr])  # type: [TpStateEntry]

        try:
            obj = pb_class()
            obj.ParseFromString(data[0].data)
            return obj
        except Exception as e:
            logger.error("Error getting or parsing data from state")
            logger.error("  class  : %s" % pb_class)
            logger.error("  address: %s" % addr)
            logger.error("  data   : %s" % data[0].data)
            raise e

    def set_for_object(self, pb_object):
        """
        Sets the state for a protobuf object based on the object type
        """
        class_name = type(pb_object).__name__
        addr = address.make_address(pb_object)  # generic address calc based on the class type
        content = pb_object.SerializeToString()

        logger.debug("setting state for %s [%s] => %r" % (class_name, addr, content))
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
            logger.info("calling '%s' with: %r" % (handler.__name__, event_data))
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

    def handle_roast_create(self, event: Roast):
        assert isinstance(event, Roast)
        self.state.set_for_object(event)

    def handle_cert_create(self, event: Certification):
        assert isinstance(event, Certification)
        self.state.set_for_object(event)

    def handle_shipment_create(self, event: Shipment):
        assert isinstance(event, Shipment)
        self.state.set_for_object(event)

    def handle_harvest_create(self, event: Harvest):
        assert isinstance(event, Harvest)
        self.state.set_for_object(event)

    def handle_farm_create(self, event):
        assert isinstance(event, Farm)
        self.state.set_for_object(event)

    def handle_add_related(self, event):
        assert isinstance(event, Events.AddRelated)

        def add(evt, obj_class, related_class, list_name):
            logger.debug("Generic Add Related")
            logger.debug("    source  : %r of %r" % (evt.object_key, obj_class))
            logger.debug("    related : %r of %r" % (evt.related_key, related_class))
            # get the state & address of the two items, using the mapping class to handle any class
            src = self.state.get_and_parse(obj_class, address.addr_map[obj_class](evt.object_key))
            related = self.state.get_and_parse(related_class, address.addr_map[related_class](evt.related_key))

            list_field = getattr(src, list_name)  # acts like a list, but really is a RepeatedScalarContext
            list_field[:] = list(set(list_field[:] + [related.key]))

            self.state.set_for_object(src)

        action_map = {
            "farm_cert": (Farm, Certification, "certifications"),
            "harvest_farm": (Harvest, Farm, "farms"),
            "harvest_shipment": (Harvest, Shipment, "shipments"),
            "roast_harvest": (Roast, Harvest, "harvests")
        }

        if event.action not in action_map:
            raise InternalError("Unmapped action for AddRelated: %s" % event.action)

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
        logger.debug("---- TRANSACTION RECIEVED ------------------------------------ ")
        evt = CoffeeChainEvents()
        try:
            evt.ParseFromString(transaction.payload)
        except DecodeError as e:
            logger.error("Error decoding message %s" % str(e))
            logger.error("  1. Object must be `CoffeeChainEvents`")
            logger.error("  2. Handler & application protobuf files must match")
            logger.error("  ---------------------------------------")
            logger.error("  body: %r" % transaction.payload)
            return

        evt_name = evt.WhichOneof('payload')
        evt_data = getattr(evt, evt_name)
        ActualHandler(context).process(evt_name, evt_data)
        logger.debug("^^^^ TRANSACTION COMPLETE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ")
