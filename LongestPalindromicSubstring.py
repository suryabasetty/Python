def longestPalindrome(self, s):
    modified = []
    for letter in s:
        modified.append(letter)
        modified.append('|')
    modified.pop()
    max_length = 0
    index = 0
    while index < len(modified):
        current_length = 0
        dist = 1
        while index - dist >= 0 and index + dist < len(modified):
            if modified[index - dist] == modified[index + dist]:
                current_length += 1
                dist += 1
            else:
                break

        max_length = max(max_length, current_length)
    return max_length