from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        q = deque([root])
        while q:
            rightNode = -1
            for _ in range(len(q)):
                curr = q.popleft()
                rightNode = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ret.append(rightNode)
        return ret
        