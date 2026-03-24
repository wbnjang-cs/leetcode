def evalRPN(tokens):
    stack = []
    operandSet = set(['+', '-', '*', '/'])
    for t in tokens:
        if t in operandSet:
            op1 = stack.pop()
            op2 = stack.pop()
            if t == "+":
                stack.append(op2 + op1)
            elif t == "-":
                stack.append(op2 - op1)
            elif t == "*":
                stack.append(op2 * op1)
            elif t == "/":
                stack.append(int(op2 / op1))
        else:
            stack.append(int(t))

        print(stack)

    return stack[0]
            


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))
