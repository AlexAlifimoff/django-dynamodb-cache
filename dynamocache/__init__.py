"Amazon DynamoDB cache backend for Django"

# Copyright (c) 2018 Alex Alifimoff <alex@sixteenzero.net>

import boto3
from django.core.files.base import ContentFile
from django.core.cache.backends.base import BaseCache

class DynamoDBCache(BaseCache):
    """
        Amazon DynamoDB cache backend for Django
    """
    def __init__(self):
        self._options = params.get('OPTIONS', {})

        self.dynamo_client = boto3.resource(region_name=self._options['REGION_NAME'])
        self.table = self.dynamo_client.Table(self._options['TABLE_NAME'])

        self.partition_key_name = self._options['PARTITION_KEY_NAME']

    def add(self, key, value, timeout=None, version=None):
        pass

    def get(self, key, default=None, version=None):
        try:
            key = {}
            key[self.partition_key_name] = key
            response = self.table.get_item(Key=key)
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['item']

    def set(self, key, value, timeout=None, version=None):
        item = {}
        item[self.partition_key_name] = key
        item['info'] = value
        item['version'] = version
        item['timeout'] = timeout
        self.table.put_item(Item=item)

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
