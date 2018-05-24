#!/bin/bash
ENDPOINT=$1
SEEDS=$2

if [[ $# -eq 0 ]] ; then
    echo 'USAGE: start_genesis_node.sh <protocol>://<endpointhostname>:<port> <comma seperated list of URIs for seeds>'
    echo 'Example: start_genesis_node.sh tcp://validator:8800 tcp://validator2:8800,tcp://validator3:8800'
    exit 0
fi

if [ -e configs/keys/*.pub ] && [ -e configs/keys/*.priv ]
then
	echo "Data already exists on first validator skipping keygen & genesis block creation"
	sawtooth-validator -vv \
         --endpoint ${ENDPOINT} \
         --seeds ${SEEDS}
	
else
	echo "No data has been found, generating the necesarry keys and start creation of genesis block"
	sawadm keygen && \
        sawtooth keygen my_key && \
        sawset genesis -k /root/.sawtooth/keys/my_key.priv && \
        sawadm genesis config-genesis.batch && \
	sawtooth-validator -vv \
	 --endpoint ${ENDPOINT} \
         --seeds ${SEEDS}
fi
