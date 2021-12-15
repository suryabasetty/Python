

def twoSum(self, nums, target):
    index = 0
    number_map = {}
    for num in nums:
        check = target - num
        if number_map.__contains__(check):
            return [index, number_map.__getitem__(check)]
        else:
            number_map[num] = index
            index += 1
    return []



