FROM python:3.6-alpine

RUN apk add --update \
        alpine-sdk \
        autoconf automake libtool \
        libffi-dev \
 && rm -rf /var/cache/apk/*

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./*.py     ./
COPY ./proto    ./proto/

RUN chmod +x processor.py
