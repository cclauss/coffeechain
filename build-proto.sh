#!/usr/bin/env bash

# builds the protobuf file and copies it & the configuration files into the
# sawtooth and server directories

# python-out is relative to the proto file itself

protoc proto/coffee.proto --python_out=./

# copy to the sawtooth transaction processor
cp proto/*.py sawtooth/proto/

# copy to the server
cp proto/*.py server/coffeechain/proto/w