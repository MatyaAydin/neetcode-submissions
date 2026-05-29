import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        for idx, e in enumerate(edges):
            u = e[0]
            v = e[1]
            adj[u].append((v, succProb[idx]))
            adj[v].append((u, succProb[idx]))
        cost = [0] * n
        cost[start_node] = 1

        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (-1, start_node))

        while pq:
            currProb, currNode = heapq.heappop(pq)
            currProb *= -1

            for neigh, neighProb in adj[currNode]:
                if cost[neigh] < currProb * neighProb:
                    cost[neigh] = currProb * neighProb
                    heapq.heappush(pq, (-cost[neigh], neigh))

        return cost[end_node]        