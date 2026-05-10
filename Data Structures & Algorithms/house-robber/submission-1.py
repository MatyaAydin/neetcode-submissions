class Solution:
	def rob(self, nums):
		n = len(nums)
		memo = [-1] * len(nums)
		def backtrack(idx):
			if idx >= n:
				return 0
			if memo[idx] != -1:
				return memo[idx]
			memo[idx] = max(nums[idx] + backtrack(idx+2), backtrack(idx+1))
			return memo[idx]
		backtrack(0)
		return max(memo)

