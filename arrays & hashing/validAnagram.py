def isAnagram(s, t):
    seen = {}
    for char in s:
        char = char.lower()
        seen[char] = seen.get(char,0) + 1
    
    for char in t:
        char = char.lower()
        if char in seen:
            seen[char] -=1
            if seen[char] == 0:
                del seen[char]
        else:
            return False
    
    if not seen:
        return True
    return False

print(isAnagram("Hello", "Olleh"))