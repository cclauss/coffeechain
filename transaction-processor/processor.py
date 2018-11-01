#!/usr/bin/env python
import argparse
import logging
import settings

from handler import CoffeeTransactionHandler
from sawtooth_sdk.processor.core import TransactionProcessor


# this should probably be in a command line parameter as well
# as in an env variable.  commandline takes precedence

def parse_args(args):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '--host',
        default=settings.VALIDATOR_HOST,
        help='Hostname for  endpoint for the validator connection'
    )

    return parser.parse_args(args)


def main(args=None):
    logging.info("Loading Transaction Processor")
    arguments = parse_args(args)
    processor = None
    try:
        url = 'tcp://%s:4004' % arguments.host
        logging.info("~ using url: %s" % url)
        processor = TransactionProcessor(url=url)
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
