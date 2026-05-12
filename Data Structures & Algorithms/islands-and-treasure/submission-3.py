from collections import deque
class Solution:
	def islandsAndTreasure(self, grid):
		if not grid:
			return grid
		m = len(grid)
		n = len(grid[0])
		q = deque([])
		shifts = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		def isValid(i, j):
			return 0 <= i < m and 0 <= j <n
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 0:
					q.append((i,j))
		while q:
			curr_x, curr_y = q.popleft()
			for dx, dy in shifts:
				neigh_x = curr_x + dx
				neigh_y = curr_y + dy
				if isValid(neigh_x, neigh_y) and grid[neigh_x][neigh_y] == 2147483647:
					if grid[neigh_x][neigh_y] > 1 + grid[curr_x][curr_y]:
						grid[neigh_x][neigh_y] = 1 + grid[curr_x][curr_y]
						q.append((neigh_x, neigh_y))
