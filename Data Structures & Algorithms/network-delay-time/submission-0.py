import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for _ in range(n+1)]
        for e in times:
            adj[e[0]].append([e[1], e[2]])

        cost = [float("inf")] * (n+1)
        cost[k] = 0
        # visited = [False] * (n+1)
        # visited[k] = True
        q = [(0, k)]
        heapq.heapify(q)

        while q:
            # print(cost)
            nodeCost, nodeIdx = heapq.heappop(q)
            for neigh in adj[nodeIdx]:
                neighIdx = neigh[0]
                transitionCost = neigh[1]
                if nodeCost + transitionCost < cost[neighIdx]:
                    # visited[neighIdx] = True
                    cost[neighIdx] = nodeCost + transitionCost
                    heapq.heappush(q, (nodeCost + transitionCost, neighIdx))

        maxCost = max(cost[1:])
        if maxCost == float("inf"):
            return -1
        return maxCost


        