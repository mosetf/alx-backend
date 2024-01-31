#!/usr/bin/python3
"""
LIFO Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class represents a Last-In-First-Out (LIFO) caching system.
    It inherits from the BaseCaching class and implements the caching
    functionality using the LIFO strategy.
    """

    def __init__(self):
        """
        Initializes a new instance of the FIFOCache class.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added to the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.
        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None
            if the key is not found in the cache.
        """
        return self.cache_data.get(key, None)
