# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIdxMap = {node: idx for idx,node in enumerate(inorder)}
        n = len(preorder)
        idx = 0

        def dfs(left, right):
            nonlocal idx
            if left > right:
                return None
            currRoot = TreeNode(preorder[idx])
            idx  += 1
            currRootIdx = inorderIdxMap[currRoot.val]

            currRoot.left = dfs(left, currRootIdx - 1)
            currRoot.right = dfs(currRootIdx + 1, right)
            return currRoot

        return dfs(0, n-1)



        