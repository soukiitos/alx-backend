#!/usr/bin/python3
'''MRU Caching'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''class MRUCache inherit from BaseCaching and is a caching system'''
    def __init__(self):
        '''Initialize LRUCache'''
        self.stack = []
        super().__init__()

    def put(self, key, item):
        '''Define put'''
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''Define get'''
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
