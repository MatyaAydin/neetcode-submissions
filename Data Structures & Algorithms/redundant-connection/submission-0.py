class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max([e[0] for e in edges] + [e[1] for e in edges])
        uf = DSU(n)
        redundantEdge = None
        for e in edges:
            if uf.createCycle(e[0], e[1]):
                redundantEdge = e
            else:
                uf.union(e[0], e[1])

        return redundantEdge


class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parents[x_root] = self.parents[y_root]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def createCycle(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        return x_root == y_root





        