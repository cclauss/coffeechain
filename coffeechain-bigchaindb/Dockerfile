FROM ubuntu:18.04

LABEL name="coffeechain-bigchaindb"
LABEL version="1.0"

RUN apt-get update && apt-get install -y \
  curl \
  build-essential

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install -y nodejs

WORKDIR /coffeechain-bigchaindb

COPY  . .

RUN npm install

EXPOSE 3000