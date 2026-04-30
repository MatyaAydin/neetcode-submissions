class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = DSU(n)
        for u,v in edges:
            createdCycle = uf.union(u,v)
            if createdCycle:
                return False
        nRoots = 0
        for nodeIdx, root in enumerate(uf.parents):
            if nodeIdx == root:
                nRoots +=1
        return nRoots == 1



class DSU:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parents[x_root] = y_root
        if x_root == y_root:
            return True
        return False

        