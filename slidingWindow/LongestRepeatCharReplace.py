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
            charCount[ord(s[l]) - ord('A')] -=1
            l +=1
        
        if r - l + 1 > maxLen:
            maxLen = r - l + 1

        r +=1
    
    return maxLen

def characterReplacementAns (s, k):
    charCount = {}
    maxLen = 0

    l = 0
    for r in range(len(s)):
        charCount[s[r]] = 1 + charCount.get(s[r], 0)

        while (r - l + 1) - max(charCount.values()) > k:
            charCount[s[l]] -=1
            l +=1

        maxLen = max(maxLen, r - l + 1)
    
    return maxLen



        


        
    
    
        
    
    


s = "ABBB"
k = 2

s1 = "AAABABBA"
k1 = 1
print(characterReplacement(s1,k1))

        
