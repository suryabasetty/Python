def mergeTwoLists(self, list1, list2):
    head = ListNode()
    ans = head
    while not (list1 == None and list2 == None):
        num_one = 101 if list1 == None else list1.val
        num_two = 101 if list2 == None else list2.val
        if num_one < num_two:
            head.next = list1
            list1 = list1.next
            head = head.next
            head.next = None
        else:
            head.next = list2
            list2 = list2.next
            head = head.next
            head.next = None
    return ans.next