#!/usr/bin/python3
'''class LIFOCache inherit from BaseCaching and is a caching system'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO Caching'''
    def __init__(self):
        '''Initialize LIFOCache'''
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
        return self.cache_data.get(key)
