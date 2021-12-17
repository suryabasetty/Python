class Solution(object):
    def isHappy(self, n):
        repeat = set()
        while n != 1 and not repeat.__contains__(n):
            repeat.add(n)
            sum = 0
            temp = n
            while (temp > 0):
                sum += (temp % 10) ** 2
                temp /= 10
                temp = int(temp)
            n = sum
        if (n == 1):
            return True
        else:
            return False
