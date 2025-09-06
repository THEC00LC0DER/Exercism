def commands(binary_str):
    this_list = []
    if binary_str[-1] == "1":
        this_list.append("wink")
    if binary_str[-2] == "1":
        this_list.append("double blink")
    if binary_str[-3] == "1":
        this_list.append("close your eyes")
    if binary_str[-4] == "1":
        this_list.append("jump")
    if binary_str[-5] == "1":
        this_list.reverse()
    return this_list