class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = 0
        n = len(nums)
        def backtrack(idx, currSum):
            nonlocal counter
            if idx == n:
                counter += (currSum == target)
                return
            currSum += nums[idx]
            backtrack(idx+1, currSum)
            currSum -= 2 * nums[idx]
            backtrack(idx+1, currSum)
            
        backtrack(0, 0)
        return counter
        