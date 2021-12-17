def climbStairs(self, n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        n -= 2
        while (n > 0):
            a = a + b
            n -= 1
            if n == 0:
                return a
            b = a + b
            n -= 1
            if n == 0:
                return b