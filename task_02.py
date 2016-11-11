#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Subclass of Exception
    Attributes:
       None
    """
    pass


def get_age(birthyear):
    """A get_age function with a manual exception.
    Args:
        birthyears(int): input of birthyear to be converted
    Returns:
        if birthyear is valid, returns age, if not returns an error
    Examples:
        >>> get_age(2099)
        Traceback (most recent call last):
        File "<pyshell#0>", line 1, in <module>
        get_age(2099)
        File "/home/vagrant/Desktop/is210-week-12-warmup/task_02.py",
        line 30, in get_age
        raise InvalidAgeError
        InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError
    else:
        return age
