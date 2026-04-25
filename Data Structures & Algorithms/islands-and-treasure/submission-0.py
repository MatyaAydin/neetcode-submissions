from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n_cols = len(grid[0])
        
        def isValid(index):
            i, j = index
            return 0 <= i < m and 0 <= j < n_cols
        
        queue = deque()
        for i in range(m):
            for j in range(n_cols):
                if grid[i][j] == 0:
                    queue.append((i, j, 1))

        while queue:
            curr_x, curr_y, cost = queue.popleft()
            shifts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in shifts:
                nx, ny = curr_x + dx, curr_y + dy
                if isValid((nx, ny)) and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = cost
                    queue.append((nx, ny, cost + 1))