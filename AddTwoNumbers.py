
def addTwoNumbers(self, l1, l2):
    cur = ListNode()
    ans = cur
    carry = 0
    while not(l1 == None and l2 == None and carry == 0):
        cur.next = ListNode()
        cur = cur.next
        num_one = 0
        num_two = 0
        if l1 != None:
            num_one = l1.val
            l1 = l1.next
        if l2 != None:
            num_two = l2.val
            l2 = l2.next
        total = num_one + num_two + carry
        carry = int (total / 10)
        cur.val = total % 10
    return ans.next