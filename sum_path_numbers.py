# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum_number(node, s):
            if not node: return s
            if not node.left and not node.right: return s*10+node.val
            return sum_number(node.left, s*10+node.val) + sum_number(node.right, s*10+node.val)
        return sum_number(root, 0)
            

root = TreeNode(4)
root.right = TreeNode(9)
root.left = TreeNode(1)
root.right.right = TreeNode(1)
s = Solution()
print(s.sumNumbers(root))