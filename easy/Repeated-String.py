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
# print (repeatedString('a', 1000000000000))