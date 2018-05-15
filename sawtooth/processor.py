#!/usr/bin/env python
import logging
import os

from sawtooth_sdk.processor.core import TransactionProcessor
from handler import CoffeeTransactionHandler

logging.basicConfig(level=logging.DEBUG)

# this should probably be in a command line parameter as well
# as in an env variable.  commandline takes precedence
VALIDATOR_HOST = os.environ.get("VALIDATOR_HOST", "localhost")

if __name__ == "__main__":
    logging.info("Starting Transaction Processor")

    processor = None
    try:
        processor = TransactionProcessor(url='tcp://%s:4004' % VALIDATOR_HOST)
        processor.add_handler(CoffeeTransactionHandler())
        processor.start()
    except KeyboardInterrupt:
        # ctrl+c handler
        pass
    except Exception as e:
        logging.error("Processor Error", exc_info=True)
    finally:
        if processor:
            processor.stop()
