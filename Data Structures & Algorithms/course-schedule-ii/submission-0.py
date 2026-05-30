from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        ordered = []
        q = deque()
        inGoing = [0] * numCourses
        for i in range(numCourses):
            for node in adj[i]:
                inGoing[node] += 1
        
        for i in range(numCourses):
            if not inGoing[i]:
                q.append(i)
                ordered.append(i)

        while q:
            curr = q.popleft()
            for node in adj[curr]:
                inGoing[node] -= 1
                if not inGoing[node]:
                    q.append(node)
                    ordered.append(node)
        if len(ordered) == numCourses:
            return ordered
        return []

        