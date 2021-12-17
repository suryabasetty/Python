def deleteDuplicates(self, head):
    temp = head
    if temp == None:
        return None
    while temp.next != None:
        next_temp = temp.next
        if temp.val == next_temp.val:
            temp.next = next_temp.next
            next_temp.next = None
        else:
            temp = temp.next
    return head