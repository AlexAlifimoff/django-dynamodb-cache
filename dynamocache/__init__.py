"Amazon DynamoDB cache backend for Django"

# Copyright (c) 2018 Alex Alifimoff <alex@sixteenzero.net>

import boto3
from botocore.exceptions import ClientError
from django.core.files.base import ContentFile
from django.core.cache.backends.base import BaseCache

class DynamoDBCache(BaseCache):
    """
        Amazon DynamoDB cache backend for Django
    """
    def __init__(self, _location, params):
        BaseCache.__init__(self, params)
        self._options = params.get('OPTIONS', {})

        self.dynamo_client = boto3.resource('dynamodb', region_name=self._options['REGION_NAME'])
        self.table = self.dynamo_client.Table(self._options['TABLE_NAME'])

        self.partition_key_name = self._options['PARTITION_KEY_NAME']

    def add(self, key, value, timeout=None, version=None):
        pass

    def get(self, k, default=None, version=None):
        try:
            key = {}
            key[self.partition_key_name] = k
            response = self.table.get_item(Key=key)
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']['info']

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

    def get_many(self, keys, version=None):
        try:
            #keys_ = []
            #for k in keys:
            #    d = {}
            #    d[self.partition_key_name] = k
            #    keys_.append(d)
            req = {'Keys': [{self.partition_key_name: k} for k in keys]}
            ri = {}
            ri[self._options['TABLE_NAME']] = req
            response = self.dynamo_client.batch_get_item(RequestItems=ri)
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']

    def set_many(self, d, timeout, version=None):
        pass


# For backwards compatibility
class CacheClass(DynamoDBCache):
    """
        Backward compatibility class definition
    """
    pass
