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

s2 = "dvdf"
s = " "
s3 = "abcabcbb"
s4 = "bbbbb"
s5 = "pwwkew"
s6 = "abba"
print(lengthOfLongestSubstring(s6))
