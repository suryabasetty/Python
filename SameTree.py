def isSameTree(self, p, q):
    if p == None and q == None:
        return True
    elif p == None or q == None:
        return False
    elif p.val == q.val:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        return False


