#!/usr/bin/env python3
'''Take two integer arguments page and page_size'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Define index_range'''
    return ((page - 1) * page_size, page * page_size)
