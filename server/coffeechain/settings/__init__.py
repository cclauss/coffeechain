from .logging import *
from ._base import *
from .sawtooth import *
from .bigchaindb import *

logger = logging.getLogger(__name__)

logger.info("DJANGO SETTINGS LOADED")
logger.info("   worker pid   = %s", os.getpid())
logger.info("   sawtooth api = %s" % SAWTOOTH_API)
logger.info("   sawtooth key = %s" % SAWTOOTH_KEY_FILE)