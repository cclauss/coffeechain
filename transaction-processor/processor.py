#!/usr/bin/env python
import logging
import os
import argparse

from sawtooth_sdk.processor.core import TransactionProcessor
from handler import CoffeeTransactionHandler

logging.basicConfig(level=logging.INFO)

# this should probably be in a command line parameter as well
# as in an env variable.  commandline takes precedence
VALIDATOR_HOST = os.environ.get("VALIDATOR_HOST", "localhost")

def parse_args(args):
    parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
    '--host',
     default= VALIDATOR_HOST,
     help='Hostname for  endpoint for the validator connection'
    )

    return parser.parse_args(args)

def main(args=None):
    logging.info("Starting Transaction Processor")
    arguments = parse_args(args)
    processor = None
    try:
        processor = TransactionProcessor(url='tcp://%s:4004' % arguments.host)
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


if __name__ == "__main__":
    main()