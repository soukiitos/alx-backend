#!/usr/bin/python3
"""
Create a class LFUCache that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''LFU Caching'''
    def __init__(self):
        '''Initialize LFUCache'''
        self.queue = []
        self.lfu = {}
        super().__init__()

    def put(self, key, item):
        '''Define put'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and \
                key not in self.cache_data:
            discarded_key = self.queue.pop(0)
            self.lfu.pop(discarded_key)
            del self.cache_data[discarded_key]
            print('DISCARD: {}'.format(discarded_key))
        if key in self.cache_data:
            self.queue.remove(key)
            self.lfu[key] += 1
        else:
            self.lfu[key] = 0
        try:
            i = self.queue.index(
                    next((k for k in self.queue if self.lfu[k] > 0), key)
                    )
            self.queue.insert(i, key)
        except ValueError:
            self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Define get'''
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.queue.index(key) + 1 != len(self.queue):
                while (self.queue.index(key) + 1 < len(self.queue) and
                        self.lfu[key] >= self.lfu[self.queue[
                            self.queue.index(key) + 1
                            ]]):
                    self.queue.insert(
                            self.queue.index(key) + 1,
                            self.queue.pop(self.queue.index(key))
                            )
        return self.cache_data.get(key)
