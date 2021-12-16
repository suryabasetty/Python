def isPalindrome(self, s):
    char_list = []
    for letter in s:
        if letter.isalnum():
            char_list.append(letter.lower())

    new_list = list(char_list)
    char_list.reverse()
    if str(new_list) == str(char_list):
        return True
    else:
        return False
