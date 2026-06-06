class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        fullSum = sum(nums)
        if fullSum % 2 != 0:
            return False
        halfSum = fullSum / 2
        n = len(nums)
        memo = defaultdict(bool)
        def backtrack(idx, currSum):
            tup = (idx, currSum)
            if idx == n:
                memo[tup] = currSum == halfSum
                return memo[tup]
            if currSum > halfSum:
                memo[tup] = False
                return memo[tup]
            
            if tup in memo:
                return memo[tup]
            # dont instantiate variable because python wont eval right if left is True
            memo[tup] = backtrack(idx+1, currSum + nums[idx]) or backtrack(idx+1, currSum)
            return memo[tup]


        backtrack(0, 0)
        return memo[(0, 0)]  


        