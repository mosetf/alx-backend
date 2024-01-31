#!/usr/bin/python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class represents a Last-In-First-Out (LIFO) caching system.
    It inherits from the BaseCaching class and implements the caching
    functionality using the LIFO strategy.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added to the cache.
        """
        pass
    
    def get(self, key):
            """
            Retrieve the value associated with the given key from the cache.

            Args:
                key: The key to retrieve the value for.

            Returns:
                The value associated with the key, or None if the key is not found in the cache.
            """
            pass
