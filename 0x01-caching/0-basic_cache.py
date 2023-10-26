#!/usr/bin/env python3
""" BAsic cache class """


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
        Add an item to the cache with the given key.

        Args:
            key: The key for the item.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the item associated with the given key from the cache.

        Args:
            key: The key to retrieve the item for.

        Returns:
            The item associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
