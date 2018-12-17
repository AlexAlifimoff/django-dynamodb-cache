"Amazon S3 cache backend for Django"

# Copyright (c) 2012,2017 Alexander Todorov <atodorov@MrSenko.com>
#
# Taken directly from django.core.cache.backends.filebased.FileBasedCache
# and adapted for S3.

import time
import hashlib

try:
    import cPickle as pickle
except ImportError:
    import pickle

from storages.backends import s3boto
from django.core.files.base import ContentFile
from django.core.cache.backends.base import BaseCache

class DynamocDBCache(BaseCache):
    """
        Amazon DynamoDB cache backend for Django
    """
    def __init__(self):
        pass

    def add(self, key, value, timeout=None, version=None):
        pass

    def get(self, key, default=None, version=None):
        pass

    def set(self, key, value, timeout=None, version=None):
        pass

    def delete(self, key, version=None):
        pass

    def has_key(self, key, version=None):
        pass

    def clear(self):
        pass

# For backwards compatibility
class CacheClass(DynamoDBCache):
    """
        Backward compatibility class definition
    """
    pass
