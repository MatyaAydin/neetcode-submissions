from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m,n = len(board), len(board[0])
        shifts = [(-1, 0), (1, 0), (0,-1), (0,1)]
        def validIdx(i,j):
            return 0 <= i < m and 0 <= j < n
        q = deque()

        for i in range(m):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "V"
            if board[i][-1] == "O":
                q.append((i, n - 1))
                board[i][-1] = "V"
        for i in range(n):
            if board[0][i] == "O":
                q.append((0, i))
                board[0][i] = "V"
            if board[-1][i] == "O":
                q.append((m - 1, i))
                board[-1][i] = "V"

        while q:
            currX, currY = q.popleft()
            for dx, dy in shifts:
                neighX, neighY = currX + dx, currY + dy
                if validIdx(neighX, neighY) and board[neighX][neighY] == "O":
                    board[neighX][neighY] = "V"
                    q.append((neighX, neighY))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "V":
                    board[i][j] = "O"

        