def largestRectangleArea(heights):
    lengthHeights = len(heights)
    stack = []
    currMax = heights[0]

    for i in range(lengthHeights):
        currI = i
        while stack and heights[i] < stack[-1][0]:
            currI = stack[-1][1]
            currMax = max(currMax, stack[-1][0] * (i - stack[-1][1]))
            stack.pop()
        
        stack.append((heights[i], currI))    

    while stack:
        currMax = max(currMax, stack[-1][0] * (lengthHeights - stack[-1][1]))
        stack.pop()

    
    return currMax

def largestRectangleAreaAns(heights):
    maxArea = 0
    stack=[] # (height, index)

    for i, h in enumerate(heights):
        start = i
        while stack and h < stack[-1][0]:
            popHeight, popIndex = stack.pop()
            start = popIndex
            maxArea = max(maxArea, popHeight * (i - popIndex))

        stack.append((h, start))    
    
    l = len(heights)
    while stack:
        popHeight, popIndex = stack.pop()
        maxArea = max(maxArea, popHeight * (l - popIndex))


    return maxArea




        


h1 = [7,1,7,2,2,4]
h2= [3,6,5,7,4,8,1,0]
h3 = [1,1]
print(largestRectangleAreaAns(h2))