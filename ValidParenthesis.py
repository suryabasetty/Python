def isValid(self, s):
    stack = []
    opposite = {}
    opposite[')'] = '('
    opposite['}'] = '{'
    opposite[']'] = '['
    for letter in s:
        if letter in ['(', '[', '{']:
            stack.append(letter)
        else:
            if len(stack) > 0 and stack.pop() == opposite[letter]:
                continue
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
