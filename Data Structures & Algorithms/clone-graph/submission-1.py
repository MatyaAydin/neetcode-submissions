from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque()
        adj = {node: Node(node.val)}
        queue.append(node)
    
        while queue:
            curr = queue.popleft()
            for neigh in curr.neighbors:
                if neigh not in adj:
                    adj[neigh] = Node(neigh.val)
                    queue.append(neigh)
                adj[curr].neighbors.append(adj[neigh])
            # print(adj)
        return adj[node]
        