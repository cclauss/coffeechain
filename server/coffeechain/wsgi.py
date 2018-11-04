"""
WSGI config for coffeechain project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import logging
import platform
import threading

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffeechain.settings")
#os.environ["BIGCHAINDB"] = 'True'  # set this in docker-compose
#os.environ["BIGCHAINDB_API"] = 'http://localhost:9984'  # set this in docker-compose

def get_thread_logstr():
    """
    Gets host/pid/thread info for logging purposes (e.g. spit out to papertrail)
    - This should probably get moved somewhere independent, not sure where though
    - maybe somewhere without django or any other dependencies in it.
    :return:
    """
    return "host={host}, pid={pid}, thread={thread}, os={os}, py={py}".format(
        pid=os.getpid(),
        host=platform.node(),
        thread=threading.current_thread().ident,
        os=platform.system(),
        py=platform.python_implementation() + " " + platform.python_version()
    )

application = get_wsgi_application()

logger = logging.getLogger(__name__)

logger.info("[COFFEECHAIN-API] UWSGI APP CREATED, ({dbg})".format(
    dbg=get_thread_logstr(),
))