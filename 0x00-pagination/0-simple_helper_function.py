#!/usr/bin/env python3
""" pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    takes page and page_size and return a tuple of integerss
    """
    end = page * page_size
    start = end - page_size
    return start, end
