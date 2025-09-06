def append(list1, list2):
    return list1 + list2 


def concat(lists):
    return [item for sublist in lists for item in sublist]


def filter(function, list):
    return [value for value in list if function(value)]

def length(list):
    return sum(1 for element in list)


def map(function, list):
    return [function(value) for value in list]


def foldl(function, list, initial):
    for value in list:
        initial = function(initial, value)
    return initial


def foldr(function, list, initial):
    for value in reverse(list):
        initial = function(initial, value)
    return initial


def reverse(list):
    number_of_elements = len(list)
    length_of_list = number_of_elements // 2
    for x in range(length_of_list):
        opposite = number_of_elements - x - 1
        list[x], list[opposite] = list[opposite], list[x]
    return list