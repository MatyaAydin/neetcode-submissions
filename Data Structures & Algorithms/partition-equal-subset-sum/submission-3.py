class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        n = len(nums)
        found = False
        memo = defaultdict(int)
        def backtrack(idx, sum1, sum2):
            tup = (idx, sum1, sum2)
            if idx == n:
                memo[tup] = (sum1 == sum2)
                return memo[tup]
            
            if tup in memo:
                return memo[tup]
            addLeft = backtrack(idx+1, sum1 + nums[idx], sum2)
            addRight = backtrack(idx+1, sum1, sum2 + nums[idx])
            memo[tup] = addLeft or addRight
            return memo[tup]


        backtrack(0, 0, 0)
        return memo[(0, 0, 0)]  


        