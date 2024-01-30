#!/usr/bin/python3
"""
FIFO caching
"""


class FIFOCache(BaseCaching):
    """
    Represents a First-In-First-Out (FIFO) cache implementation.

    This cache follows the FIFO eviction policy, where the least
    recently used item is evicted
    when the cache reaches its maximum capacity.

    Inherits from the BaseCaching class.
    """

    def __init__(self):
        """
        Initializes a new instance of the FIFOCache class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.

        Args:
            key: The key to associate with the item.
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
