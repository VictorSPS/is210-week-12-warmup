#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """A function with exception handling.
    Args:
        var1(any): input value for function
        var2(any): input value for function
    Return:
        returns an error message if invalid input
    Examples:
        >>> simple_lookup([1, 2], 4)
        Warning: Your index/key doesn't exist.
        [1, 2]
    """
    try:
        var1[var2]
    except(IndexError, KeyError):
        print "Warning: Your index/key doesn't exist."
        return var1
