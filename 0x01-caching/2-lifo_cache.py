#!/usr/bin/env python3
""" FIFO cache  """

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    this class implement Last In First Out
    caching policies
    """
    def __init__(self):
        """ initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assign item to keys
        and sort cache base on LIFO
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed_key = next(reversed(self.cache_data))
                del self.cache_data[removed_key]
                print('DISCARD: {}'.format(removed_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        return the key associate to each item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
