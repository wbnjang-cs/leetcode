def dailyTemperatures(temperatures):
    result=[0] * len(temperatures)
    stack=[(temperatures[0], 0)]

    for i in range(1, len(temperatures)):
        temp = temperatures[i]

        while stack and stack[-1][0] < temp:          
            result[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        
        stack.append((temp,i))

    return result

def dailyTemperaturesFaster(temperatures):
    result = [0] * len(temperatures)
    stack=[]

    for i in range(len(temperatures)):
        temp = temperatures[i]
        while stack and temp > temperatures[stack[-1]]:
            day = stack.pop()
            result[day] = i - day
        
        stack.append(i)
    
    return result

def dailyTemperaturesRe(temperatures):
    res = [0] * len(temperatures)
    stack = [(temperatures[0], 0)] #tuple is temperature, day

    for i in range(1, len(temperatures)):
        currTemp = temperatures[i]
        while stack and currTemp > stack[-1][0]:
            topDay = stack[-1][1]
            res[topDay] = i - topDay
            stack.pop()
        stack.append((currTemp, i))

    return res

def dailyTemperaturesReBetter(temperatures):
    res = [0] * len(temperatures)
    stack = [0] #stack only has days

    for i in range(1, len(temperatures)):
        currTemp = temperatures[i]
        while stack and currTemp > temperatures[stack[-1]]:
            day = stack.pop()
            res[day] = i - day
            
        stack.append(i)

    return res

