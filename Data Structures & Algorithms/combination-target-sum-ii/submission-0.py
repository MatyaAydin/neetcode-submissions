class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        candidates.sort()
        n = len(candidates)
        def backtrack(curr, currSum, idx):
            if currSum == target:
                solutions.append(curr[:])
                return
            if idx == n or currSum > target:
                return

            curr.append(candidates[idx])
            backtrack(curr, currSum+ candidates[idx], idx+1)
            curr.pop()
            while idx+1 < n and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(curr, currSum, idx+1)
            

        backtrack([], 0, 0)
        return solutions
        