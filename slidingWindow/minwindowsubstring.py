from collections import defaultdict

def minWindowAns(s, t):
    if t == "":
        return ""
    
    #the indexes and the length of the substring
    res = [-1,-1]
    resLen = float("infinity")

    #dictionar for the characters and their frequencies in t
    tCount = defaultdict(int)
    for char in t:
        tCount[char] +=1
    
    #dictionary for character count in window
    window = defaultdict(int)

    #For checking many of the characters we have enough of
    need = len(tCount)
    #have is the number of characters in t that the window has enough of
    have = 0
    
    l = 0
    for r in range(len(s)):
        c = s[r]
        #increment amount of c in window
        window[c] +=1

        #if c is in tCount, and we got enough for the first time, have +=1
        if c in tCount and window[c] == tCount[c]:
            have +=1
        
        #Once the window is a valid answer
        while have == need:
            
            #if the substring is shorter than what we have, update
            if (r-l + 1) < resLen:
                res = [l,r]
                resLen = r - l + 1
            
            #we keep moving the left pointer forwards, updating window count as we go
            window[s[l]] -=1
            #if we remove a character in tCount, we need to check if we still have enough of that character
            #checking if window is still valid after removing char
            if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                have -=1
            l +=1
    
    #if resLen is still infinity, we never found a valid window
    return s[res[0]: res[1] + 1] if resLen != float("infinity") else ""


            



            
    return s[l: r]

        
    print(l,i)
    return windowCount == tCount
            
        


s = "ADOBECODEBANC"
t = "ABC"

s2 = "OUZODYXAZV"
t2 = "XYZ"

s3 = "ab"
t3 = "b"
print(minWindow(s2,t2))