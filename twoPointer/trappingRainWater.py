def trap(height):
    i = 0
    j = len(height) - 1
    
    maxL = height[i]
    maxR = height[j]
    rain = 0

    while i < j:
        if maxL <= maxR:
            i +=1
            rain += max(maxL - height[i], 0)
            maxL = max(maxL, height[i])     
        else:
            j -=1
            rain += max(maxR - height[j], 0)
            maxR = max(maxR, height[j])

    
    return rain

def trapAns(height):
    #for empty lists
    if not height:
        return 0;

    #two pointers, one on each side
    l = 0
    r = len(height) - 1
    
    #We start the maxL and maxR as the ends of the list
    maxL = height[l]
    maxR = height[r]
    rain = 0

    #once l >= r, we found the water for each height
    #Water at each height is min(maxL, maxR) - (height of that bar)
    #The smaller of the tallest wall on the left and right 
    # determines how much water can be stored at a height.
    #similar to containerMostWater
    while l < r:
        #if maxL < maxR, then that means maxL is the limiting factor. so we move it up
        #  and calculate how much rain can be stored
        if maxL < maxR:
            l +=1
            #we can update maxL first because if maxL is smaller than height[l]
            #it would be negative and we would make it 0 before adding anyways.
            #By updating first one less thing to check (is maxL - height[l] == 0)
            maxL = max(maxL, height[l])
            rain += maxL - height[l]
        #if maxR <= maxL, maxR is limiting so move it down
        else:
            r -=1
            maxR = max(maxR, height[r])
            rain += maxR - height[r]
    
    return rain








        

h = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [4,2,0,3,2,5]
print(trap(h2))