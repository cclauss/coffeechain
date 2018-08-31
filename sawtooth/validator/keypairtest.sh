#!/bin/bash
IFS=$'\n'
GETKEYS=`node -e "console.log(require('zeromq').curveKeypair())"`
echo $GETKEYS > keypair.txt 
