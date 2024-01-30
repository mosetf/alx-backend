#!/usr/bin/python3
"""
FIFO caching
"""


class FIFOCache(BaseCaching):    """
    Represents a First-In-First-Out (FIFO) cache implementation.

    This cache follows the FIFO eviction policy, where the least
    recently used item is evicted
    when the cache reaches its maximum capacity.

    Inherits from the BaseCaching class.
    """
    def __init__(self):
        
