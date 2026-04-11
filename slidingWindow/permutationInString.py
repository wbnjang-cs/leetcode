def checkInclusion(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) > len(s2):
        return False
    
    winLen = len(s1)
    #Should change to s1Count
    ans = [0 for i in range(26)]
    #Should change to windowCount
    seen = [0 for i in range(26)]
    
    l = 0
    r = winLen
    
    #What the list should look like
    for i in range(winLen):
        ans[ord(s1[i]) - ord('a')] +=1

    #What the list looks like for the first (winLen) characters
    for i in range(r):
        seen[ord(s2[i]) - ord('a')] +=1

    #move sliding window to end
    while r < len(s2):
        #if current window matches answer, return True
        if seen == ans:
            return True
        
        #add the next character to the window
        seen[ord(s2[r]) - ord('a')] +=1
        r +=1
        #remove last charcter as l moves to right
        seen[ord(s2[l]) - ord('a')] -=1
        l +=1
     
    if seen == ans:
        return True
    return False


def checkInclusionAns(s1, s2):
    #if s1 longer than s2, s2 can't contain s1
    if len(s1) > len(s2):
        return False
    
    #list that represents how many of each alphabet there is
    s1Count = [0] * 26
    s2Count = [0] * 26

    #Fill list for both strings
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] +=1
        s2Count[ord(s2[i]) - ord('a')] +=1
    
    #instead of comparing list each time, keep track of how many indexes match
    matches = 0
    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches +=1
    
    #left is beginning, r starts at where we left off
    l = 0
    for r in range(len(s1), len(s2)):
        #if all 26 match, return True
        if matches == 26:
            return True
        
        #find letter of right pointer and increment
        index = ord(s2[r]) - ord('a')
        s2Count[index] +=1
        #if incrementing made a match, increment number of matches
        if s2Count[index] == s1Count[index]:
            matches += 1
        #if incrementing made us 1 bigger than match, then we lost a match
        elif s2Count[index] == s1Count[index] + 1:
            matches -= 1

        #find letter of left pointer and decrement
        index = ord(s2[l]) - ord('a')
        s2Count[index] -=1
        #if decrementing made a match, increment number of matches
        if s2Count[index] == s1Count[index]:
            matches += 1
        #if decrementing made us 1 smaller than a match, then we lost a match
        elif s2Count[index] == s1Count[index] - 1:
            matches -= 1

        l +=1

    #loop doesn't check matches for final window
    if matches == 26:
        return True
    return False
