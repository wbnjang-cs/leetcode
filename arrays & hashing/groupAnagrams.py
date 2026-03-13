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

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
        
    




