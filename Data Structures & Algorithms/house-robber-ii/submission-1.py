class Solution:
	def rob(self, nums):
		if len(nums) == 1:
			return nums[0]
		return max(self.robSimple(nums[1:]), self.robSimple(nums[:-1]))
		
	def robSimple(self, nums):
		n = len(nums)
		memo = [-1] * n
		def backtrack(idx):
			if idx >= n:
				return 0
			if memo[idx] != -1:
				return memo[idx]
			memo[idx] = max(nums[idx] + backtrack(idx +2), backtrack(idx+1))
			return memo[idx]
		backtrack(0)
		return max(memo)
		
