def maxDepth(self, root):
    return self.get_height(root, 0)


def get_height(self, root, height):
    if root == None:
        return height
    return max(self.get_height(root.left, height + 1), self.get_height(root.right, height + 1))