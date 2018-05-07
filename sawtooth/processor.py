import logging

from sawtooth_sdk.processor.core import TransactionProcessor
from handler import CoffeeTransactionHandler

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.info("Starting Transaction Processor")

    processor = None
    try:
        processor = TransactionProcessor(url='tcp://localhost:4004')
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
