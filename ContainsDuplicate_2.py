def containsNearbyDuplicate(self, nums, k):
    left = 0
    right = 0
    unique = set()
    while right < len(nums):
        if right - left <= k:
            if unique.__contains__(nums[right]):
                return True
            unique.add(nums[right])
            right += 1
        else:
            unique.remove(nums[left])
            left += 1
    return False