from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0
        m = len(grid)
        n = len(grid[0])

        def isValidIndex(i,j):
            return 0 <= i < m and 0 <= j < n

        def BFS(grid, source):

            IslandArea = 0
            queue = deque()
            queue.append(source)
            grid[source[0]][source[1]] = 0
            IslandArea +=1

            while queue:
                curr_x, curr_y = queue.popleft()
                # neigh = []
                # for d_x in [-1, 0, 1]:
                #     for d_y in [-1, 0, 1]:
                #         if d_x == d_y: continue
                #         neigh.append((curr_x + d_x, curr_y + d_y))

                neigh = [
                    (curr_x+1, curr_y),
                    (curr_x-1, curr_y),
                    (curr_x, curr_y+1),
                    (curr_x, curr_y-1),
                ]

                for n_x, n_y in neigh:
                    if isValidIndex(n_x, n_y) and grid[n_x][n_y] == 1:
                        queue.append((n_x, n_y))
                        grid[n_x][n_y] = 0
                        IslandArea +=1

            return IslandArea


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = BFS(grid, (i,j))
                    maxArea = max(maxArea, area)
                    # print(maxArea)

        return maxArea
        