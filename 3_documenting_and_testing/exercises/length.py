#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining the lenght of a list

Created on 20/12/2024
@author: Ahmed Khalifa
"""


# def length(a) -> int:
#   if len(a) == 0:
#       return None
#   else:
#       return len(a)

def length(a: list) -> int:
    """
    Calculate the length of a list.

    Parameters:
        a: list

    Returns -> int

    Raises:    
        AssertionError: if  the argument is not a list

    >>> length([])
    0

    >>> length([3])
    1

    >>> length([3, 3])
    2

    >>> length([1,2,4,5,6,7,8,0,0,4])
    10
    """

    assert isinstance(a, list), "'a' is not a list"

    if len(a) == 0: # Check if the list is empty
        return None
    else:
        return len(a) # Returns the list's length
