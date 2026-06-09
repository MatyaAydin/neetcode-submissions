class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        matrix_zero = [[i for i in m] for m in matrix]
        m,n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix_zero[i][j] == 0:
                    for k in range(m):
                        matrix[k][j] = 0
                    for k in range(n):
                        matrix[i][k] = 0  