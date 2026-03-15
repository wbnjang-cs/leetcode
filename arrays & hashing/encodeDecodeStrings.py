def encode(strs):
    result = ""
    for word in strs:
        result = result + str(len(word)) + "?" + word
    return result

def decode(s):

    result = []
    word = ""
    length = ""
    while(len(s) != 0):
        while(s[0] != "?"):
            length += s[0]
            s = s[1:]
        
        result.append(s[1:int(length) + 1])
        length = ""
    return result

def decodeBetter(s):
    index = 0
    result = []
    length = ""

    while(index < len(s)):
        markTracker = index
        while(s[markTracker] != "?"):
            markTracker +=1
        
        length = int(s[index:markTracker])
        result.append(s[markTracker + 1 : markTracker + length + 1])
        index = markTracker + 1 + length
    return result
    


dummy1 = ["we","say",":","yes","!@#$%^&*()"]
dummy2 = ["0"] #
dummy3 = ["hello", "world"]

# print(encode(dummy1))
# print(encode(dummy2))
# print(encode(dummy3))

# print(decodeBetter(encode(dummy1)))
# print(decodeBetter(encode(dummy2)))
print(decodeBetter(encode(dummy3)))



