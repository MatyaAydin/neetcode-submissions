from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        maxCost = 0
        freshCount = 0

        def validIndex(coord):
            i,j = coord
            return 0 <= i < m and 0 <= j < n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j, 1))
                    visited[i][j] = True
                if grid[i][j] == 1:
                    freshCount +=1
        while queue and freshCount > 0:
            curr_x, curr_y, cost = queue.popleft()
            shifts = [(-1, 0), (1, 0), (0, 1), (0,-1)]
            neigh = [(curr_x + dx, curr_y + dy) for dx, dy in shifts if validIndex((curr_x + dx, curr_y + dy))]
            for nx, ny in neigh:
                if grid[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    grid[nx][ny] = 2
                    queue.append((nx,ny, cost+1))
                    maxCost = max(maxCost, cost)
                    freshCount -=1
        if freshCount != 0:
            return -1
        return maxCost



        
        