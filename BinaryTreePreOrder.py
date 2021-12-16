class Solution(object):
    def preorderTraversal(self, root):
        order = []
        self.getPreOrder(root, order)
        return order

    def getPreOrder(self, root, order):
        if root == None:
            return
        order.append(root.val)
        self.getPreOrder(root.left, order)
        self.getPreOrder(root.right, order)
