## Building

    # build and tag as coffeechain-api:latest by default
    docker build -t coffeechain-api .

## Running

    # run the api as standard, and remove the container
    docker run --rm coffeechain-api

    # to run a shell, override the entrypoint
    docker run -it --rm --entrypoint="/bin/sh" coffeechain-api

    # change the worker count, or pass other env vars
    docker run --rm -e WORKERS=2 coffeechain-api

## Notes

- Entrypoint is /app/entrypoint-gunicorn.sh
- Gunicorn listens on 0.0.0.0:8000