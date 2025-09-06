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
SUBLIST = "List One Sublist Of List Two"
SUPERLIST = "List One Superlist Of List Two"
EQUAL = "Equal Lists"
UNEQUAL = "Unequal Lists"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST

    def is_sublist(small, large):
        return any(small == large[index:index+len(small)] for index in range(len(large) - len(small) + 1))
        # large[i: i+len(small)] slices to the amount of elements in the smaller list

    if len(list_one) < len(list_two):
        return SUBLIST if is_sublist(list_one, list_two) else UNEQUAL
    return SUPERLIST if is_sublist(list_two, list_one) else UNEQUAL


