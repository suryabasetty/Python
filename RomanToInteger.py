def romanToInt(self, s):
    roman = dict()
    roman['I'] = 1
    roman['V'] = 5
    roman['X'] = 10
    roman['L'] = 50
    roman['C'] = 100
    roman['D'] = 500
    roman['M'] = 1000
    min = 0
    sum = 0
    for letter in reversed(s):
        cur = roman[letter]
        if cur >= min:
            sum += cur
            min = cur
        else:
            sum -= cur
    return sum