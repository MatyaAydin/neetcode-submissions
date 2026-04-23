from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numOfIslands = 0
        m = len(grid)
        n = len(grid[0])

        def isValidIndex(i,j):
            return 0 <= i < m and 0 <= j < n

        def BFS(grid, source):
            queue = deque()
            queue.append(source)
            grid[source[0]][source[1]] = "0"

            while queue:
                curr_x, curr_y = queue.popleft()

                neigh = [
                    (curr_x-1, curr_y),
                    (curr_x+1, curr_y),
                    (curr_x, curr_y-1),
                    (curr_x, curr_y+1),
                ]

                for n in neigh:
                    n_x, n_y = n
                    if isValidIndex(n_x, n_y) and grid[n_x][n_y] == "1":
                        grid[n_x][n_y] = "0"
                        queue.append((n_x, n_y))
            return grid




        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid = BFS(grid, (i,j))
                    numOfIslands +=1


        return numOfIslands
        


