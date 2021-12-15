def isPalindrome(self, x):
    if x < 0:
        return False
    new_num = 0
    num = x
    while x > 0:
        new_num *= 10
        new_num += x % 10
        x /= 10
    if num == new_num:
        return True
    else:
        return False
