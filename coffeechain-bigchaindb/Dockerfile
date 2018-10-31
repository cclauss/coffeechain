FROM node:8.12.0-alpine

WORKDIR /coffeechain-bigchaindb

COPY  . .

RUN apk add --no-cache --virtual .build-deps make gcc g++ python && \
    npm install && \
    npm cache clean --force && \
    apk del .build-deps

EXPOSE 3000