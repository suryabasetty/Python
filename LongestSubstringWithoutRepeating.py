
def lengthOfLongestSubstring(self, s):
    left = 0
    right = 0
    unique = set()
    word = str(s)
    max_length = 0
    while right < len(word):
        # print(word.__getitem__(right))
        if unique.__contains__(word.__getitem__(right)):
            while word.__getitem__(left) != word.__getitem__(right):
                unique.remove(word.__getitem__(left))
                left += 1
            left += 1
            right += 1
        else:
            max_length = max(max_length, right - left + 1)
            unique.add(word.__getitem__(right))
            right += 1
    return max_length

