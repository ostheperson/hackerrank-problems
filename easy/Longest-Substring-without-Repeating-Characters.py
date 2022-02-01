
"""
str = 'abcbabcd'
longest - 'abcd'
output - 4

1. get letter
2. add letter to string if not in string
3. if seen letter: 
    if hash table does not have key string
        add our string to a hash table [string] 
        then we reset the string
    else: increment hash string
4. go to 1
5. add string to hash if not in hash else increment
6. return lenght of longest hash key (string)
"""

def longSubStr(myString):
    # do stuff
    longestSubstring = ''
    hashTable = {}
    for i in myString:
        # check if seen letter
        if i in longestSubstring:
            # check if string is in hash
            if longestSubstring not in hashTable:
                # add to hash table
                hashTable[longestSubstring] = 1
                longestSubstring = ''
            else: 
                #increment
                hashTable[longestSubstring] += 1
                longestSubstring = ''
            longestSubstring += i
        else:
            # add i to longestSubstring
            longestSubstring += i
            # print (longestSubstring)
    # once done
    if longestSubstring not in hashTable:
        # add to hash table
        hashTable[longestSubstring] = 1
        longestSubstring = ''
    else: 
        #increment
        hashTable[longestSubstring] += 1
    maxx = 0
    for x in hashTable.keys():
        maxx = len(i) if len(i) > maxx else maxx
    return maxx

print(longSubStr('abcabbcabcd'))