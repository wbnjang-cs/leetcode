from collections import deque

def isValid(s):
    myStack = deque()

    for c in s:
        if c == ")":
            try:
                if myStack.pop() == "(":
                    continue
                else:
                    return False
            except:
                return False
            
        elif c == "]":
            try:
                if myStack.pop() == "[":

                    continue
                else:
                    return False
            except:
                return False
            
        elif c == "}":
            try:
                if myStack.pop() == "{":
                    continue
                else:
                    return False
            except:
                return False
        
        else:
            myStack.append(c)

    if not myStack:

        return True
    
    return False


def isValidAns(s):
    stack = deque()
    map = {")" : "(", "}" : "{", "]" : "["}

    for c in s:
        if c in map:
            if not stack or stack.pop() != map[c]:
                return False
        else:
            stack.append(c)
    
    if stack:
        return False
    
    return True

s = "[()]"

print(isValidAns(s))