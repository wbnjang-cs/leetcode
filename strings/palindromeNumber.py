def isPalindrome(x):
    if x < 0:
        return False
    
    dig = 1
    t = 10
    digitsDict = {0:x%t}
    while(x > t):
        t *=10
        digitsDict[dig] = int((x % t) // (t/10))
        dig +=1
    
    t = 0
    for i in range(len(digitsDict)):
        t += digitsDict[i] * 10 ** (len(digitsDict)-i-1)
    
    return x == t


def isPalindromeAnswer(x):
    if x < 0:
        return False
    
    reversedHalf = 0
    while(x > reversedHalf):
        #Take what we have, move it over so the 1's digit is empty, then we put in the last digit of x
        reversedHalf = reversedHalf * 10 + x // 10
        #remove the digit we moved over to reversed half
        x = x//10
    
    #or is there for odd lengths, becaus the middle digit will be in the reversed half, we drop it by doing //10 and then compare
    return x == reversedHalf or x == reversedHalf//10
    

    


