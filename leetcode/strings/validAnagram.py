def isAnagram(s, t):
    d = {}
    for char in s:
        if char in d.keys():
            d[char] +=1
        else:
            d[char] = 1

    
    for char in t:
        if char not in d.keys():
            return False
        else:
            d[char] -=1
            if d[char] == 0:
                del d[char]
    
    if not d:
        return True
    else:
        return False

#Good Job!
def isAnagramOptimized(s, t):

    if len(s) != len(t):
        return False
    
    d = {}
    for char in s:
        #dictionary.get(key x, int y) is basically if key exists, return its value, otherwise, return y
        #in this case, it checks if d[char] exists, it returns the value, adds one, and updates. otherwise, it returns 0, +1, then update
        d[char] = d.get(char, 0) + 1

    
    for char in t:
        #this defaults to keys, no need for d.keys() Ever!
        if char not in d:
            return False
        d[char] -=1
    
    return all(v == 0 for v in d.values())
    #what it does
    #1. v == 0 for v in d.values() : check all values in d, and return True/False for each
    #2. all() : returns True if all is true, false if all is not true


#Super Clean way
# from collections import Counter
# def isAnaGramSuperOptimized(s, t):
#     return Counter(s) == Counter(t)
#Counter is a dictionary optimized for counting things, its in C so it is often faster.