#!/usr/bin/python3
"""Basic dictionary"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    '''Inherit from BaseCaching and is a caching system'''

    def put(self, key, item):
        '''Define put'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''Define get'''
        return self.cache_data.get(key, None)
