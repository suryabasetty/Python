def majorityElement(self, nums):
    count = 0
    majority = sys.maxsize
    for num in nums:
        if num == majority:
            count += 1
        elif count > 0:
            count -= 1
        else:
            count = 1
            majority = num
    return majority

