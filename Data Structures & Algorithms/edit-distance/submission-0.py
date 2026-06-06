class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        tab = [[0] * (n1+1) for _ in range(n2+1)]
        for i in range(n1+1):
            tab[0][i] = i
        for i in range(n2+1):
            tab[i][0] = i

        for i in range(1, n2+1):
            for j in range(1, n1+1):
                if word1[j-1] == word2[i-1]:
                    tab[i][j] = tab[i-1][j-1]
                else:
                    tab[i][j] = 1 + min(min(tab[i-1][j], tab[i][j-1]), tab[i-1][j-1])

        return tab[-1][-1]
        