#!/bin/sh
# for apline linux, uses sh not bash

gunicorn coffeechain.wsgi:application \
    --name "CoffeeChain API" \
    --bind=0.0.0.0:8000 \
    --workers=${WORKERS:-2} \
    --forwarded-allow-ips="*"