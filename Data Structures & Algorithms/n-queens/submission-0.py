class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        def validBoard(board):
            # idx i in board is row idx of queen i, board[i] is col idx of queen i
            if len(set(board)) != len(board):
                return False
            for i in range(len(board)):
                for j in range(i+1, len(board)):
                    if abs(i - j) == abs(board[i] - board[j]):
                        return False
            return True

        def backtrack(board, idx):
            if idx == n:
                grid = [["."] * n for _ in range (n)]

                for idx_, pos in enumerate(board):
                    grid[idx_][pos] = "Q"
                grid = ["".join(r) for r in grid]
                solutions.append(grid[:])
                return

            for i in range(n):
                board[idx] = i
                if validBoard(board[:idx+1]):
                    backtrack(board, idx + 1)




        backtrack([0] * n, 0)
        return solutions

        