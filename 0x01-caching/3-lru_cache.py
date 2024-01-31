#!/usr/bin/python3
''' LRU Caching'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''class LRUCache inherit from BaseCaching and is a caching system'''
    def __init__(self):
        '''Initialize LRUCache'''
        self.queue = []
        super().__init__()

    def put(self, key, item):
        '''Define put'''
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        '''Define get'''
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
