class MinStack(object):

    def __init__(self):
        self.stack = []
        self.currentMin = 0
        

    def push(self, val):
        if not self.stack:
            self.currentMin = val

        if val < self.currentMin:
            self.currentMin = val

        self.stack.append((val, self.currentMin))

        #print(f"after push, stack is {self.stack}")

    def pop(self):
        if len(self.stack) >= 2:
            self.currentMin = self.stack[-2][1]
        self.stack.pop()

        #print(f"after pop, stack is {self.stack} and min is {self.currentMin}")

        

    def top(self):
        #print("getting top")
        return self.stack[-1][0]
        

    def getMin(self):
        #print("getting min")
        return self.stack[-1][1]
    
class MinStackAns(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val):
        self.stack.append(val)
        if not self.minStack:
            curMin = val
        else:
            curMin = min(val, self.minStack[-1])
        self.minStack.append(curMin)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        #print("getting min")
        return self.minStack[-1]
    


minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # expected: -3

minStack.pop()
print(minStack.top())     # expected: 0
print(minStack.getMin())  # expected: -2

minStack.push(2)
minStack.push(-4)
minStack.push(3)
print(minStack.getMin())  # expected: -4

minStack.pop()
print(minStack.getMin())  # expected: -4

minStack.pop()
print(minStack.top())     # expected: -4
print(minStack.getMin())  # expected: -4

minStack.pop()
print(minStack.top())     # expected: 2
print(minStack.getMin())  # expected: -2