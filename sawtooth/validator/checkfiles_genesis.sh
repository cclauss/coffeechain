#!/bin/bash

if [ -e configs/keys/*.pub ] && [ -e configs/keys/*.priv ]
then
	echo "Data already exists on first validator skipping keygen & genesis block creation"
	exit 0
else
	sawadm keygen && \
        sawtooth keygen my_key && \
        sawset genesis -k /root/.sawtooth/keys/my_key.priv && \
        sawadm genesis config-genesis.batch
fi
