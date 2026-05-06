class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minCost = 0
        uf = DSU(n)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                edges.append([i, j, manhattanDistance(points[i], points[j])])
        edges.sort(key=lambda e: e[2])
        # print(edges)
        added = 0
        for u,v,w in edges:
            if uf.union(u, v):
                minCost += w
                added +=1
        # print(added)
        return minCost


def manhattanDistance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

class DSU:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        self.parents[x_root] = y_root
        return True
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
        