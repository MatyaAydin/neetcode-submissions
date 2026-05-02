class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = DSU(n)
        for e in edges:
            uf.union(e[0], e[1])
        nComponents = 0
        for idx, root in enumerate(uf.parents):
            nComponents += idx == root
        return nComponents
        

class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parents[x_root] = y_root
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
        