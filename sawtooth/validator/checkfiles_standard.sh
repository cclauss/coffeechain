#!/bin/bash

if [ -e configs/keys/*.pub ] && [ -e configs/keys/*.priv ]
then
	echo "Data already exists on validator skipping keygen"
	exit 0
else
	sawadm keygen
fi
