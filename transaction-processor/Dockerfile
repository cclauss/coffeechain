FROM python:3.6-alpine

WORKDIR /app
COPY requirements.txt    .

RUN \
    # this virtual package can be uninstalled after the python requirements are built
    apk add --update --no-cache --virtual docker-build-deps \
        alpine-sdk \
        autoconf automake libtool \
    # these deps are required for the running system
&&  apk add --update --no-cache --virtual docker-runtime-libs \
        libffi-dev \
        libzmq \
    # upgrade pip & so on.  not usually necessary, but does prevent some build issues sometimes
&&  pip install --upgrade pip wheel setuptools \
    # install the requirements here so we can remove the apk packages after
&&  pip install -r requirements.txt \
    # remove the build deps virtual package
&&  apk del docker-build-deps

COPY ./*.py     ./
COPY proto    ./proto/

RUN chmod +x processor.py

ENTRYPOINT python processor.py --host ${VALIDATOR}

# ENV VARIABLES
# These variables should be supplied to the container at runtime
#
# Name -------- Format ---------------- Default ------------
# VALIDATOR     Host Name               None

# If you prefer, ou can manually set the validator that this TP should connect to
# in the docker-compose file or on the command line:
#
#    entrypoint: python processor.py --host {validator host name}
