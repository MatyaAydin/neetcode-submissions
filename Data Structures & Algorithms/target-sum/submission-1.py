class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def backtrack(idx, currSum):
            tup = (idx, currSum)
            if idx == n:
                memo[tup] = currSum == target
                return memo[tup]
            if tup in memo:
                return memo[tup]
            
            tupPlus = backtrack(idx+1, currSum + nums[idx])
            tupMinus = backtrack(idx+1, currSum - nums[idx])
            memo[tup] = tupPlus + tupMinus
            return memo[tup]
            
        backtrack(0, 0)
        return memo[(0, 0)]
        