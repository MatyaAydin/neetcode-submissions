class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        fullSum = sum(nums)
        if fullSum % 2 != 0:
            return False
        halfSum = fullSum / 2
        n = len(nums)
        memo = defaultdict(bool)
        def backtrack(idx, sum1, sum2):
            tup = (idx, sum1, sum2)
            if idx == n:
                memo[tup] = (sum1 == sum2)
                return memo[tup]
            if sum1 > halfSum or sum2 > halfSum:
                memo[tup] = False
                return memo[tup]
            
            if tup in memo:
                return memo[tup]
            memo[tup] = backtrack(idx+1, sum1 + nums[idx], sum2) or backtrack(idx+1, sum1, sum2 + nums[idx])
            return memo[tup]


        backtrack(0, 0, 0)
        return memo[(0, 0, 0)]  


        