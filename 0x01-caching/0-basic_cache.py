#!/usr/bin/python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that extends the BaseCaching class.
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__(self)

    def put(self, key, item):
        """
        Add an item to the cache with the specified key.

        Args:
            key: The key to associate with the item.
            item: The item to be added to the cache.
        """
        if key is None or item is None:
            return 
        self.cache_data[key] = item

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
