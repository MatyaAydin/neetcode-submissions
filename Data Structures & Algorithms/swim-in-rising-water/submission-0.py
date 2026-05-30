import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def validIdx(i,j):
            return 0 <= i < m and 0 <= j < n

        shifts = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]
        
        pq = []
        heapq.heapify(pq)
        costs = [[float("inf")] * n  for _ in range(m)]
        costs[0][0] = grid[0][0]
        heapq.heappush(pq, (grid[0][0], (0, 0)))

        while pq:
            currTime, currNode = heapq.heappop(pq)
            currX, currY = currNode
            if currX == m - 1 and currY == n - 1:
                break
            for dx,dy in shifts:
                neighX = currX + dx
                neighY = currY + dy
                if validIdx(neighX, neighY):
                    neighTime = grid[neighX][neighY]
                    latest = max(currTime, neighTime)
                    if latest < costs[neighX][neighY]:
                        costs[neighX][neighY] = latest
                        heapq.heappush(pq, (latest, (neighX, neighY)))
        return costs[m-1][n-1]

        