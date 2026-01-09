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


print(isPalindrome(12321))

