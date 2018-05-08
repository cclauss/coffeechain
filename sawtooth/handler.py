import logging

from sawtooth_sdk.processor.exceptions import InternalError
from sawtooth_sdk.processor.handler import TransactionHandler

from proto.config import TXF_NAME, ADDRESS_PREFIX, TXF_VERSIONS
from proto.coffee_pb2 import *
from proto import address


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
        logging.debug("got transaction")
        evt = CoffeeChainEvents()
        evt.ParseFromString(transaction.payload)
        evt_name = evt.WhichOneof('payload')

        handler = getattr(self, "handle_%s" % evt_name, None)
        if handler:
            logging.info("calling %s" % evt_name)
            logging.info("%r" % evt)
            handler(getattr(evt, evt_name), context)
        else:
            raise InternalError("No handler for %s" % evt_name)

    def set_state(self, context, pb_object):
        class_name = type(pb_object).__name__
        addr = address.make_address(pb_object)
        content = pb_object.SerializeToString()[:]

        print("setting state for %s [%s] => %r" % (class_name, addr, content))
        address_out = context.set_state({
            addr: content
        })
        if not address_out:
            raise InternalError("Error setting state for message %s" % class_name)
        else:
            logging.debug("set state calculated address: %s" % address_out)

    def handle_mint_code(self, event: Events.MintCode, context):

        code = Code(
            message=event.message,
            company_id=3,
        )
        print("code:", code.SerializeToString())
        self.set_state(context, code)

    def handle_cert_create(self, event: Certification, context):

        self.set_state(context,event)

    def handle_harvest_create(self, event: Harvest, context):

        self.set_state(context,event)


    #
    #
    #     harbat = Harvest(
    #         id=event.id,
    #         month=event.month,
    #         year=event.year
    #
    #     )
    #     print("harvest batch:",harbat.SerializeToString())
    #     self.set_state(context, harbat)
