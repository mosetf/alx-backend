#!/usr/bin/python3
"""
LIFO Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class represents a Least Frequently Used (LFU) caching system.
    It inherits from the BaseCaching class and implements the caching
    functionality using the LFU strategy.
    """

    def __init__(self):
        """
        Initializes a new instance of the LFUCache class.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.key_freq = []
    
    def __reorder_items(self, mru_key):
        """
        Reorders the items in the cache based on the Most Recently Used (MRU) key.

        Args:
            mru_key (Any): The key of the Most Recently Used (MRU) item.
        Returns:
            None
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
            """
            Add or update an item in the cache.

            Args:
                key: The key of the item.
                item: The item to be added or updated.
            """
                    
