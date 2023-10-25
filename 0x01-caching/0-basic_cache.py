#!/usr/bin/env python3
""" BAsic cache class"""
BaseCaching = __import__('BaseCaching').BaseCaching


class BasicCache(BaseCaching):
    """
    This is BAsic cache that use put and get
    """
    def __init__(self):
        """
        initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        put an item into cache using key
        """
        if key or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        return the value of caches linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
