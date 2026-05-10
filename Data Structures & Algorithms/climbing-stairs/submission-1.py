class Solution:
	def climbStairs(self, n):
		memo = defaultdict(int)
		def backtrack(runningSum):
			if runningSum == n:
				return 1
			if runningSum > n:
				return 0
			if runningSum in memo:
				return memo[runningSum]
			from1 = backtrack(runningSum+1)
			from2 = backtrack(runningSum+2)
			memo[runningSum] = from1 + from2
			return memo[runningSum]


		backtrack(0)
		return memo[0]
			
		
