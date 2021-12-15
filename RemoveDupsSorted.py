def removeDuplicates(self, nums):
    if len(nums) == 0:
        return 0
    min = -101
    insert = 0
    check = 0
    while check < len(nums):
        current = nums[check]
        if (min < current):
            nums[insert] = current
            min = current
            insert += 1
        check += 1
    return insert
