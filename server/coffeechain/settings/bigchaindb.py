from ._base import env

BIGCHAINDB_ENABLED = bool(env.str('BIGCHAINDB_ENABLED', 'False'))
BIGCHAINDB_API = env.str('BIGCHAINDB_API', 'http://localhost:9984/')