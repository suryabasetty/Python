def containsDuplicate(self, nums):
    unique = set()
    for num in nums:
        if unique.__contains__(num):
            return True
        unique.add(num)
    return False
