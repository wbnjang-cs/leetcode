def maxArea(heights):
    i = 0
    j = len(heights) -1
    maxArea = 0

    while i < j:
        leftWall = heights[i]
        rightWall = heights[j]

        currArea = abs(i-j) * min(leftWall, rightWall)
        if currArea > maxArea:
            maxArea = currArea
        
        if leftWall < rightWall:
            i +=1
        else:
            j -=1

    return maxArea

h1 = [1,7,2,5,4,7,3,6]
print(maxArea(h1))

h2 = [2,2,2]
print(maxArea(h2))