def isPalindrome(s):
    i = 0
    j = len(s) -1

    while i < j:
        while not s[i].isalnum():
            i +=1
            if i == len(s):
                return True

        while not s[j].isalnum():
            j -=1
        
        if s[i].lower() != s[j].lower():
            return False
        
        i +=1
        j -=1

    return True

#        print(f"comp {s[i]} to {s[j]}")
        


s = "A man, a plan, a canal: Panama"
s1 = "     "
s2="Was it a car or a cat I saw?"
s3 = "."
s4 = ",."
print(isPalindrome(s))
print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalindrome(s3))
print(isPalindrome(s4))