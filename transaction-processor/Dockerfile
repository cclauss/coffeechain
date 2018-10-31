FROM python:3.6-alpine

WORKDIR /app
COPY ../server/requirements.txt .

RUN \
    # this virtual package can be uninstalled after the python requirements are built
    apk add --update --no-cache --virtual docker-build-deps \
        alpine-sdk \
        autoconf automake libtool \
    # these deps are required for the running system
&&  apk add --update --no-cache --virtual docker-runtime-libs \
        libffi-dev \
        libzmq \
    # install the requirements here so we can remove the apk packages after
&&  pip install -r requirements.txt \
    # remove the build deps virtual package
&&  apk del docker-build-deps

COPY ./*.py     ./
COPY proto    ./proto/

RUN chmod +x processor.py
