def commands(binary_str):
    commands = ("wink", "double blink", "close your eyes", "jump")
    binary_commands = [command for index, command in enumerate(commands) if binary_str[4-index] == "1"]
    if binary_str[0] == "1":
        binary_commands.reverse()
    return binary_commands