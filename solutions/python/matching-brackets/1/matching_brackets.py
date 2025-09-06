def is_paired(input_string: str) -> bool:
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}  

    for character in input_string:
        if character in brackets.values():  
            stack.append(character)
        elif character in brackets: 
            if not stack or stack.pop() != brackets[character]:
                return False  

    return len(stack) == 0  