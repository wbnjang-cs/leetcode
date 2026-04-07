def lengthOfLongestSubstring(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)

    l = 0
    seen = set()
    max = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l +=1
        
        seen.add(s[r])
        if r - l + 1> max:
            max = r - l + 1
    
    return max
    


s = "abcabcbb"
s2 = "xxxx"
s3 = "pwwkew"
s4 = "tmmzuxt"
print(lengthOfLongestSubstring(s))


        


    