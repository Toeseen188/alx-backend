#!/usr/bin/env python3
""" pagination """
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int)-> Tuple[int, int]:
    """
    takes page and page_size and return a tuple of integerss
    """
    end = page * page_size
    start = end - page_size
    return start, end


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
        get page returns the dataset after using index range to paginate it
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        if not dataset or page > len(dataset) or page_size > len(dataset):
            return []
        start, end = index_range(page, page_size)
        return dataset[start:end]
