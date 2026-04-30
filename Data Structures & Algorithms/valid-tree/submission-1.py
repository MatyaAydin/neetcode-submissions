class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        uf = DSU(n)
        for u,v in edges:
            uf.union(u,v)
        nRoot = 0
        for k in uf.parents.keys():
            if k == uf.parents[k]:
                nRoot += 1
        return nRoot == 1
    


class DSU:
    def __init__(self, n):
        self.parents = {i:i for i in range(n)}

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parents[x_root] = y_root

        