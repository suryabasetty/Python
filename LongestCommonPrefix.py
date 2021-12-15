def longestCommonPrefix(self, strs):
    index = 0
    flag = True
    while flag:
        letter = ' '
        if index < len(strs[0]):
            letter = strs[0].__getitem__(index)
        else:
            index -= 1
            break
        for word in strs:
            if index < len(word) and letter == word.__getitem__(index):
                continue
            else:
                flag = False
                index -= 2
                break
        index += 1

    if index == -1:
        return ""
    else:
        return strs[0][0:index + 1]