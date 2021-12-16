def postorderTraversal(self, root):
    order = []
    self.getPostOrder(root, order)
    return order


def getPostOrder(self, root, order):
    if root == None:
        return
    self.getPostOrder(root.left, order)
    self.getPostOrder(root.right, order)
    order.append(root.val)

