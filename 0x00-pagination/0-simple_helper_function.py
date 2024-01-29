#!/usr/bin/env python3
""" Simple helper function """
from typing import List


def index_range(page: int , page_size: int) -> List[int]:
    """
    Return a tuple of the start and end indices for the given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices.

    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
