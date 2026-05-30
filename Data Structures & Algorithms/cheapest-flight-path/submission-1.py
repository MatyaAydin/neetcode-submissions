class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k stops -> at most k node between src and dst, i.e, visit k + 1 edges

        cost = [float("inf")] * n
        cost[src] = 0

        for i in range(k+1):
            tmpcost = [c for c in cost]
            for u, v, w in flights:
                if cost[v] > tmpcost[u] + w:
                    cost[v] = tmpcost[u] + w

        if cost[dst] == float("inf"):
            return -1
        return cost[dst]
        