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