def isBalanced(self, root):

    check = self.validate(root, 0)
    if check[1] == True:
        return True


def validate(self, root, height):
    if root == None:
        return [height, True]
    left_check = self.validate(root.left, height + 1)
    right_check = self.validate(root.right, height + 1)
    height = max(left_check[0], right_check[0])
    if (left_check[1] and right_check[1] and abs(left_check[0] - right_check[0]) <= 1):
        return [height, True]
    else:
        return [height, False]