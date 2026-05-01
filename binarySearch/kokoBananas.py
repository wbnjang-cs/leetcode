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
