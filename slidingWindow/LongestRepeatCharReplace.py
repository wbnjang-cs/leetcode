from collections import defaultdict

def characterReplacement(s, k):
    l = 0
    r = 0
    maxLen = 0
    freqCharVal = 0
    charCount = [0 for i in range(26)]
    
    while r < len(s):
        charVal = ord(s[r]) - ord('A')
        charCount[charVal] +=1
        if charCount[charVal] > charCount[freqCharVal]:
            freqCharVal = charVal
        
        while r - l + 1 - charCount[freqCharVal] > k:
            #Was Missing this line so code didn't work
            charCount[ord(s[l]) - ord('A')] -=1
            #------------------------------------------
            l +=1
        
        if r - l + 1 > maxLen:
            maxLen = r - l + 1

        r +=1
    
    return maxLen

def characterReplacementAns (s, k):
    #Will keep track of Char : frequency of Char INSIDE THE WINDOW
    charCount = {}
    #will return this value
    maxLen = 0

    l = 0
    for r in range(len(s)):
        charCount[s[r]] = 1 + charCount.get(s[r], 0)

        #The window is valid while (r - l + 1) - max(charCount.values()) > k
        # length of window - (num of most frequent character) > number of swaps
        #Basically can we swap the non-most frequent characters to get all the same character

        #This loop checks if the window is valid.
        #if not valid, it will move the left pointer until window is valid
        #while updating charCount accordingly
        while (r - l + 1) - max(charCount.values()) > k:
            charCount[s[l]] -=1
            l +=1

        #update maxLen
        maxLen = max(maxLen, r - l + 1)
    
    return maxLen

def characterReplacementAnsBetter(s, k):
    
    charCount = {}
    maxLen = 0

    l = 0
    maxFreq = 0
    for r in range(len(s)):
        charCount[s[r]] = 1 + charCount.get(s[r], 0)


        maxFreq = max(maxFreq, charCount[s[r]])

        #The largest possible window will always be when the maxFreq is the highest
        #lower maxFreq only leads to smaller windows, so we don't even need to check
        while (r - l + 1) - maxFreq > k:
            charCount[s[l]] -=1
            l +=1

        maxLen = max(maxLen, r - l + 1)
    
    return maxLen


        
