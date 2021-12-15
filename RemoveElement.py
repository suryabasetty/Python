def removeElement(self, nums, val):
    insert = 0
    check = 0
    while check < len(nums):
        current = nums[check]
        if current != val:
            nums[insert] = current
            insert += 1
        check += 1
    return insert