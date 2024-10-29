#!/usr/bin/env python3
"""add method takes two integer arguments with default value 1 and 10"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple containing a start index and an end index"""
    return (page * page_size) - page_size, (page * page_size)


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
        """return the appropriate page of the dataset"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        first, last = index_range(page, page_size)
        if first > len(self.dataset()):
            return []
        return self.dataset()[first:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing the following key-value pairs"""
        first, last = index_range(page, page_size)
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if last < len(self.__dataset) else None,
            'prev_page': page - 1 if first > 0 else None,
            'total_pages': math.ceil(len(self.__dataset) / page_size)
        }