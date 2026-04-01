def maxArea(heights):
    #start from widest square, two pointers on each side
    i = 0
    j = len(heights) -1
    maxArea = 0

    #if pointers overlap we are done, we hit every height
    while i < j:
        leftWall = heights[i]
        rightWall = heights[j]
        #calculate area
        currArea = abs(i-j) * min(leftWall, rightWall)

        #update maxArea when necessary
        if currArea > maxArea:
            maxArea = currArea
        
        #move the pointer on the side that has the shorter wall.
        #THis is the only way that the area can grow

        #if we moved the bigger wall down, we would have a shorter
        #width but the height would still be limited by the same short wall we left
        if leftWall < rightWall:
            i +=1
        else:
            j -=1

    return maxArea



h1 = [1,7,2,5,4,7,3,6]
print(maxArea(h1))

h2 = [2,2,2]
print(maxArea(h2))