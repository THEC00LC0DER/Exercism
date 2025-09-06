"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from enum import Enum


class ListComparison(Enum):
    SUBLIST = 1
    SUPERLIST = 2
    EQUAL = 3
    UNEQUAL = 4


SUBLIST = ListComparison.SUBLIST
SUPERLIST = ListComparison.SUPERLIST
EQUAL = ListComparison.EQUAL
UNEQUAL = ListComparison.UNEQUAL


def is_sublist(small, large):
    len_of_small, len_of_large = len(small), len(large)
    return any(small == large[i:i + len_of_small] for i in range(len_of_large - len_of_small + 1))


def sublist(list_one, list_two):
    if list_one == list_two:
        return ListComparison.EQUAL

    if is_sublist(list_one, list_two):
        return ListComparison.SUBLIST
    if is_sublist(list_two, list_one):
        return ListComparison.SUPERLIST
    return ListComparison.UNEQUAL


