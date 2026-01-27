from collections import deque

def isValid(s):
    d = deque()
    v = ["()", "[]", "{}"]
    for char in s:
        if char == '(' or char == '[' or char == '{':
           d.append(char)
        elif len(d) == 0:
            return False
        elif d[-1] + char in v:
            d.pop()
        else:
            return False
    
    return len(d) == 0

def isValidAnswer(s):
    stack = []
    match = {')' : '(', ']' : '[', '}' : '{'}

    for char in s:
        if char in match:
            if len(stack) == 0 or stack[-1] != match[char]:
                return False
            stack.pop()

        else:
            stack.append(char)
    
    return len(stack == 0)






