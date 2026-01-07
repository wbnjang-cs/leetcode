def reverseString(s):
    t = ""
    l = len(s)
    for i in range(l//2, l):
        t = s[i]
        s[i] = s[l-i-1]
        s[l-i-1] = t

def reverseStringAnswer(s):
    s[:] = s[::-1]


s = ["h","e","l","p","o"]
reverseString(s)
print(s)