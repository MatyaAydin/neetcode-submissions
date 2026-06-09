class Solution:
    def partition(self, s: str) -> List[List[str]]:
        allSubstrings = []
        n = len(s)

        def backtrack(currList, idx):
            if idx == n:
                allSubstrings.append(currList[:])
                return
            # backtrack(currList, idx + 1)
            for j in range(idx, n):
                substr = s[idx:j+1]
                if substr == substr[::-1]:
                    currList.append(substr)
                    backtrack(currList, j+1)
                    currList.pop()
                    # backtrack(currList, j+1)
        backtrack([], 0)
        return allSubstrings

            
