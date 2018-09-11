# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

from __future__ import unicode_literals

from django.conf import settings

from redis import StrictRedis


def get_strict_redis(host=None, port=None, db=None):
    """Retrieves Redis client object (StrictRedis) according to configuration.
    """
    host = host or settings.REDIS_HOSTNAME
    port = port or settings.REDIS_PORT
    db = db if db is not None else settings.REDIS_DB_ID
    client = StrictRedis(host=host, port=port, db=db)
    return client