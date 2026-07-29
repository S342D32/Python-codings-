def parenthesis(s):
    stack = []
    matched = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matched.values():  # Check if it's an opening bracket
            stack.append(char)
        elif char in matched.keys():  # Check if it's a closing bracket
            if stack == [] or matched[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

# Create an instance of Solution to test
print(parenthesis("(){}[]"))  # Output: True
print(parenthesis("({[)]}"))  # Output: False
print(parenthesis("([{}])"))  # Output: True
