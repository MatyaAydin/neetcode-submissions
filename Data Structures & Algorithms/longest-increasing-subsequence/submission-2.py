class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # only need to keep track of last element in the curr subsequence
        n = len(nums)
        memo = defaultdict(int)
        def backtrack(idx, lastAddedIdx):
            tup = (idx, lastAddedIdx)
            if idx == n:
                return 0
            if tup in memo:
                return memo[tup]
            picked = 0
            if lastAddedIdx == -1 or nums[idx] > nums[lastAddedIdx]:
                picked = 1 + backtrack(idx+1, idx)
            skipped = backtrack(idx+1, lastAddedIdx)
            memo[tup] = max(picked, skipped)
            return memo[tup]


        backtrack(0, -1)
        return memo[(0, -1)]
        