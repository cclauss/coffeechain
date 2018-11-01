import logging.config
import os

VALIDATOR_HOST = os.environ.get("VALIDATOR_HOST", "localhost")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

# Matches the output format used by the python api server
logging.config.dictConfig({
    "version": 1,
    'disable_existing_loggers': False,
    "loggers": {
        "": {
            "level": LOG_LEVEL,
            "handlers": ["console"],
            "propagate": False,
        },
        "handler": {
            "level": "DEBUG", "handlers": ["console"], "propagate": False
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": "ext://sys.stdout"
        },
    },
    "formatters": {
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)5s] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        }
    }
})
