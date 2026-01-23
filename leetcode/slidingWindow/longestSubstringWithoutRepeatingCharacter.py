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
        
s2 = "dvdf"
s = " "
s3 = "abcabcbb"
s4 = "bbbbb"
s5 = "pwwkew"
s6 = "abba"
print(lengthOfLongestSubstring(s6))
