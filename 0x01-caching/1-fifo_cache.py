#!/usr/bin/env python3
"""
INFO CACHE
"""
from collections import OrderedDict
BaseCaching = __import__('BaseCaching').BaseCaching


class FIFOCache(BaseCaching):
    """
    info cache class
    """
    def __int__(self):
        """
        initialize
        """
        super().__int__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put method to assign item to key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed_key = next(iter(self.cache_data))
                del self.cache_data[removed_key]
                print("DISCARD: {}".format(removed_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        return cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
