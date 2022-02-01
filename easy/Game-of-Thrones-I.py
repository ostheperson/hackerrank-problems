def gameOfThrones(word) -> bool:
    unique_word = set([char for char in word])
    res = 'YES'
    if len(word) % 2 == 0:
        for char in unique_word:
            if word.count(char) % 2 != 0:
                res = 'NO'
                break
    else:
        seenUnique = 0
        for char in unique_word:
            if word.count(char) % 2 != 0:
                seenUnique += 1
                if seenUnique > 1:
                    res = 'NO'
                    break
    return res