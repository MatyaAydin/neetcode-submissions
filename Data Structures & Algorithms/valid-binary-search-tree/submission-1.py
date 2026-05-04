# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isValid(root, -float("inf"), float("inf"))


    
def isValid(root, lb, ub):
    if not root:
        return True
    if lb < root.val < ub:
        return isValid(root.left, lb, root.val) and isValid(root.right, root.val, ub)
    else:
        return False
        