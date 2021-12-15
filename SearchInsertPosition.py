def searchInsert(self, nums, target):
    return self.find(nums, target, 0, len(nums) - 1)


def find(self, nums, target, start_index, end_index):
    if start_index > end_index:
        return start_index
    else:
        mid = int((start_index + end_index) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.find(nums, target, start_index, mid - 1)
        else:
            return self.find(nums, target, mid + 1, end_index)