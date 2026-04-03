from collections import defaultdict

def groupAnagrams(strs):
    anagramGroups = {}
    returnList = []

    for word in strs:
        sortedWord = "".join(sorted(word))
        if sortedWord not in anagramGroups:
            anagramGroups[sortedWord] = []
        anagramGroups[sortedWord].append(word)
    
    for value in anagramGroups:
        returnList.append(anagramGroups[value])
    
    return returnList

def groupAnagramsAns(strs):
    result = defaultdict(list)

    for s in strs:
        #each index represents an alphabet
        letterCount = [0] * 26

        #for each character increment the 
        #corresponding place in the letterCount list by 1
        for char in s:
            #ord = get unicode value
            #same as ascii for chars
            letterCount[ord(char) - ord('a')] +=1
        
        #turn list into tuple = can us as dict key
        result[tuple(letterCount)].append(s)
    
    #put all values of dict into list
    return list(result.values())


def groupAnagramsRe(strs):
    result = []
    anagSeen = {}

    for str in strs:
        sortStr = "".join(sorted(str))

        if sortStr not in anagSeen:
            anagSeen[sortStr] = [str]
        else:
            anagSeen[sortStr].append(str)
    
    for l in anagSeen.values():
        result.append(l)
    return result


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagramsAns(strs))
        
    




