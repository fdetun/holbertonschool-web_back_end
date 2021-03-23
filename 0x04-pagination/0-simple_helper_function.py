#!/usr/bin/env python3
"""
Main file
"""

def index_range(page, page_size):
    """index_range function"""

    if page != 1:
        return (page, page_size*page)
    return (0, page_size)