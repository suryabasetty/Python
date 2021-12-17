def merge(self, nums1, m, nums2, n):
    insert = m + n - 1
    first = m - 1
    second = n - 1
    while first >= 0 or second >= 0:
        first_ele = nums1[first] if first >= 0 else -sys.maxsize
        second_ele = nums2[second] if second >= 0 else -sys.maxsize

        if first_ele > second_ele:
            nums1[insert] = first_ele
            first -= 1
        else:
            nums1[insert] = second_ele
            second -= 1
        insert -= 1
    return