FROM python:3.6-alpine

WORKDIR /app
COPY ./requirements.txt .

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

COPY ./*.py         ./
COPY ./coffeechain  ./coffeechain/
COPY ./scripts      ./scripts/

# create the .env file
RUN touch .env 

# generate the private key file for this specific image of the processor
# this is best for testing.  however it means that different builds will
# have different keys, and can't be used together on the same network
RUN python manage.py migrate
RUN python manage.py runscript make_private_key

# set up the entrypoint file, and add as the default entrypoint for the container
COPY ./entrypoint-gunicorn.sh ./
RUN chmod +x ./entrypoint-gunicorn.sh

# use entrypoint so we can still have ctrl^c ability from the console when using docker run without "-it"
ENTRYPOINT ["/app/entrypoint-gunicorn.sh"]