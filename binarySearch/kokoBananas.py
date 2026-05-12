def minEatingSpeed(piles, h):
    #We are searching binary searching from 1 (The slowest possible eating speed) to max(piles) (The fastest eating speed Koko could ever need)
    i = 1
    j = max(piles)

    #For tracking minSpeed and the hours it takes to finish at each speed
    minSpeed = j
    currHours = 0

    #O(log(m)), where m is max of piles
    #Binary search
    while i <= j:
        #IMPORTANT, THIS WAS THE STEP I FORGOT AND CAUSED PROBLEMS
        currHours = 0
        #IMPORTANT, THIS WAS THE STEP I FORGOT AND CAUSED PROBLEMS

        #current speed
        mid = i + (j-i) // 2

        #Calculate how much time it takes to finish all piles at current speed (O(n))
        for pile in piles:
            currTime = - (-pile // mid)
            currHours += currTime
        
        #Takes too long, we are eating too slow. Raise lower boundry
        if currHours > h:
            i = mid+1

        #We might be able to go slower, lower upper boundry
        else:
            #Update minSpeed if necessary
            if mid < minSpeed:
                minSpeed = mid
            j = mid-1
    
    return minSpeed

def minEatingSpeedRe(piles, h):
    #slowest eating speed is 1, not 1
    i = 1
    #important
    j = max(piles)

    minSpeed = j
    
    while i <= j:
        m = (i + j) // 2
        time = 0

        for pile in piles:
            time += - (-pile // m)
        
        if time > h:
            i = m + 1
        elif time <= h:
            j = m - 1
            minSpeed = min(m, minSpeed)

    return minSpeed
p1 = [30,11,23,4,20]
h1 = 5

print(minEatingSpeed(p1, h1))