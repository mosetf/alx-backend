#!/usr/bin/env python3
""" Simple helper function """
from typing import List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> List[int]:
    """
    Return a tuple of the start and end indices for
    the given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices.

    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The data corresponding to the specified page.
        """
        # checks if the passed values are of type int
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        indices = index_range(page, page_size)
        start_index, end_index = indices

        return self.dataset()[start_index:end_index]
    def get_hyper(self, page: int, page_size: int) -> Dict:
        """
        Retrieve hypermedia pagination information.
        
        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing hypermedia
            pagination information.
        """
        x = self.dataset()
        start, end = index_range(page, page_size)
        total_pages = (len(x) + page_size - 1) // page_size
        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if end < len(self.__dataset) else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_pages": total_pages
        }
