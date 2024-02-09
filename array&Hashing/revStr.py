st = 'my name is khan!'

def reverseStr(s):
    newS = ''
    for i in range(len(s)-1, -1, -1):
        newS += s[i]
    return newS

print(reverseStr(st))
