import logging
import logging.config 

# gunicorn_logger = logging.getLogger("gunicorn.error")
# if gunicorn_logger:
#     gunicorn_logger.info("running inside gunicorn")

# Match the output format of gunicorn (expected context)
# I could not find a way to add our loggers to the existing gunicorn ones 
# and re-use that, so opted for this way.  We expect to be running inside gunicorn
LOGGING_CONFIG=None
logging.config.dictConfig({
    "version": 1,
    'disable_existing_loggers': False,
    "loggers": {
        "coffeechain": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
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
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        }
    }
})