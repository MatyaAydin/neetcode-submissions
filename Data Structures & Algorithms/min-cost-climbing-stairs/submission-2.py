class Solution:
	def minCostClimbingStairs(self, cost):
		n = len(cost)
		memo = [-1] * n
		def backtrack(idx):
			if idx >= n:
				return 0
			if memo[idx] != -1:
				return memo[idx]
			memo[idx] = min(cost[idx] + backtrack(idx+1), cost[idx] + backtrack(idx+2))
			return memo[idx]
		backtrack(0)
		return min(memo[0], memo[1])
