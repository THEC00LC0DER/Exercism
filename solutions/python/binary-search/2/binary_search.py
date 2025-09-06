def find(search_list, value):
    search_list = sorted(search_list)
    print(search_list)
    upper = len(search_list) - 1
    lower = 0
    mid = (upper + lower) // 2 
    while lower <= upper:
        mid = (upper + lower) // 2 
        currentValue = search_list[mid]
        if currentValue == value:
            return mid 
        elif currentValue > value:
            upper = mid - 1
        else:
            lower = mid + 1
    raise ValueError("value not in array")


