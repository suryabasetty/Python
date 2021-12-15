def lengthOfLastWord(self, s):
    words = s.strip()
    wordstart = 0
    l = len(words)
    for index in range(0, l):
        if (words.__getitem__(l - 1 - index) != ' '):
            continue
        else:
            wordstart = l - index
            break
    return l - wordstart
