class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        shifts = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        found = False
        def validIdx(x, y):
            return 0 <= x < m and 0 <= y <n

        def backtrack(curr, x, y, visited):
            nonlocal found
            currword = "".join(curr)
            # print(currword)
            if currword == word:
                found = True
                return

            for dx, dy in shifts:
                nx = dx + x
                ny = dy + y
                if validIdx(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    curr.append(board[nx][ny])
                    backtrack(curr, nx, ny, visited)
                    visited[nx][ny] = False
                    curr.pop()

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                visited[i][j] = True
                backtrack([board[i][j]], i, j, visited)
        return found

        