import hashlib

TXF_NAME = "coffeechain"
TXF_VERSION = "1.0.1"
TXF_VERSIONS = [TXF_VERSION]  # multiple versions here will register this TP once for each
ADDRESS_PREFIX = hashlib.sha512(TXF_NAME.encode('utf-8')).hexdigest()[0:6]
