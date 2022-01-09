def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i != len(c) - 1:
        if i + 1 < len(c):
            if c[i+1] == 0:
                jumps += 1
                i += 1
        if i + 2 < len(c):
            if c[i+2] == 0:
                jumps += 1
                i += 2
            else:
                if c[i+1] == 0:
                    jumps += 1
                    i += 1
    return jumps