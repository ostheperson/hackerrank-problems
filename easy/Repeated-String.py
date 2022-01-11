"""
aba
1. mainString = reproduce the string of n lenght
    i = 1
    loop through i % len(str) && i <= n
2. find 'a'
3. count 'a' 
4. increase i by 1
4. return count

get no of a in s
mainString = n//len(s) * (s + s[n%len(s)])
"""


def repeatedString(s, n):
    mainStr = ''
    aInS = len([x for x in s if x == 'a'])
    if n % len(s) == 0:
        count = int(aInS * (n/len(s)))
        
    else:
        multi = n//len(s)
        extra = s[0: n-(len(s)*multi)]
        aInExtra = len([x for x in extra if x == 'a'])
        count = ( aInS * multi ) + aInExtra
    return count
print (repeatedString('a', 1000000000000))