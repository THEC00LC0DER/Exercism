"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.

from enum import Enum


class ListComparison(Enum):
    SUBLIST = "List One Sublist Of List Two"
    SUPERLIST = "List One Superlist Of List Two"
    EQUAL = "Equal Lists"
    UNEQUAL = "Unequal Lists"

SUBLIST = ListComparison.SUBLIST
SUPERLIST = ListComparison.SUPERLIST
EQUAL = ListComparison.EQUAL
UNEQUAL = ListComparison.UNEQUAL

def sublist(list_one, list_two):
    if list_one == list_two:
        return ListComparison.EQUAL
    if not list_one:
        return ListComparison.SUBLIST
    if not list_two:
        return ListComparison.SUPERLIST

    is_sublist = lambda small, large: any(small == large[index:index+len(small)] for index in range(len(large) - len(small) + 1))

    if is_sublist(list_one, list_two):
        return ListComparison.SUBLIST
    if is_sublist(list_two, list_one):
        return ListComparison.SUPERLIST
    return ListComparison.UNEQUAL


