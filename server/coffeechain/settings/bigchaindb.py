from coffeechain.common.constants import Chain
from ._base import env, CHAIN

if CHAIN == Chain.BIGCHAIN:
    BIGCHAINDB_API = env.str('BIGCHAINDB_API', 'http://localhost:9984/')
else:
    BIGCHAINDB_API = None
