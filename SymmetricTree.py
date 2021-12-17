def isSymmetric(self, root):
    if root == None:
        return True
    else:
        return self.isMirror(root.left, root.right)


def isMirror(self, root_one, root_two):
    if root_one == None and root_two == None:
        return True
    elif root_one == None or root_two == None:
        return False
    elif root_one.val == root_two.val:
        return self.isMirror(root_one.left, root_two.right) and self.isMirror(root_one.right, root_two.left)
    else:
        return False