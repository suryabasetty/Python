class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root == None:
            return False
        elif root.left == None and root.right == None and root.val == targetSum:
            return True
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
