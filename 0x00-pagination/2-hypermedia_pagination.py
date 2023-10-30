#!/usr/bin/env python3
""" pagination """
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[int, int]:
        """ takes in page and page_size as arguments
        then return dictionary key: values
        """
        mydict = {}
        dataset = self.dataset()
        total_pages = len(dataset)
        total_pages = math.ceil(total_pages / page_size)
        dataset_page = self.get_page(page, page_size)
        mydict['page_size'] = len(dataset_page)
        mydict['page'] = page
        mydict['data'] = dataset_page
        if page >= 1 and page_size >= 1:
            if page_size <= len(dataset_page):
                prev_page = page - 1
                next_page = page + 1
            else:
                next_page = None
            if page > 1:
                next_page = page + 1
                prev_page = page - 1
            else:
                prev_page = None
            if len(dataset_page) <= 0:
                next_page = None
        mydict['next_page'] = next_page
        mydict['prev_page'] = prev_page
        mydict['total_pages'] = total_pages
        return mydict
