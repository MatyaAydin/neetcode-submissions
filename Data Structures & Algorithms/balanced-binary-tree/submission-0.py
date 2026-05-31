# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def traverse(root):
            nonlocal balanced

            if not root:
                return 0
  
            leftHeight = traverse(root.left) + 1
            rightHeight = traverse(root.right) + 1

            if abs(leftHeight - rightHeight) > 1:
                balanced = False
            return max(leftHeight, rightHeight)
        traverse(root)
        return balanced
        