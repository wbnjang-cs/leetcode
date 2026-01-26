#longestSubstringWithoutRepeatingCharacter.py

def lengthOfLongestSubstring(s):
    longest = 0
    startingPoint = 0

    seen = {}

    for i in range(len(s)):
        char = s[i]
        if char in seen:
            longest = max(longest, i - startingPoint)
            
            startingPoint = max(startingPoint, seen[char] + 1)
            del seen[char]

        
        seen[char] = i
    
    longest = max(longest, len(s) - startingPoint)

    return longest

def lengthOfLongestSubstringAns(s):
    seen = {}
    left = 0
    longest = 0

    for right, char in enumerate(s):
        if char in seen:
            left = max(left, seen[char]+1)
        
        seen[char] = right
        longest = max(longest, right-left+1)
    
    return longest

def lengthOfLongestResolve(s):
    seen = {}
    left = 0
    maxLength = 0

    for right, c in enumerate(s):
        if c in seen:
            left = max(left, seen[c] + 1)
        seen[c] = right
        maxLength = max(maxLength, right-left+1)
    
    return maxLength

        

