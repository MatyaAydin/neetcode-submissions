from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def validIdx(i,j):
            return 0 <= i < m and 0 <= j < n

        shifts = [(-1, 0), (1, 0), (0, -1), (0,1)]

        source_p = []
        source_a = []
        for i in range(m):
            source_p.append([i, 0]) # left side
            source_a.append([i, n-1]) # right side
        for i in range(n):
            source_p.append([0, i]) # upper side
            source_a.append([m-1, i]) # lower side

        def BFS(sources):
            reached = set([(x,y) for x,y in sources])
            visited = [[False]*n for _ in range(m)]
            for i,j in sources:
                visited[i][j] = True
            q = deque(sources)
            while q:
                curr_x, curr_y = q.popleft()
                neigh = []
                for dx,dy in shifts:
                    if validIdx(dx+curr_x, dy+curr_y):
                        neigh.append([dx+curr_x, dy+curr_y])
                for neigh_x, neigh_y in neigh:
                    # >= because must look at where water could have come from
                    if not visited[neigh_x][neigh_y] and heights[neigh_x][neigh_y] >= heights[curr_x][curr_y]:
                        visited[neigh_x][neigh_y] = True
                        q.append([neigh_x, neigh_y])
                        reached.add((neigh_x, neigh_y))
            return reached

        reached_p = BFS(source_p)
        reached_a = BFS(source_a)

        return [[x,y] for x,y in reached_p if (x,y) in reached_a]

        