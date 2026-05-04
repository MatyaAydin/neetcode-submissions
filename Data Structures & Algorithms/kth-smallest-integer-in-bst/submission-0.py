# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        ret = 0

        def inorder(node):
            nonlocal counter
            nonlocal ret

            if not node:
                return
            inorder(node.left)
            counter +=1
            if counter == k:
                ret = node.val
            inorder(node.right)

        inorder(root)
        return ret


            

        