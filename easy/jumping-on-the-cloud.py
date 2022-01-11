def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i != len(c) - 1:
        if i + 2 < len(c):
            if c[i+2] == 0:
                jumps += 1
                i += 2
            elif c[i+1] == 0:
                jumps += 1
                i += 1
        elif i + 1 < len(c):
            if c[i+1] == 0:
                jumps += 1
                i += 1
    return jumps

"""
1. find a 0
2. jump to zero
3. increase count by 1
4. repeat 1 till end of array
"""