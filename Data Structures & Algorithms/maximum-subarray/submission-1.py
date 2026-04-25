class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        extending = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            extending = max(extending + nums[i], nums[i])
            maxSum = max(maxSum, extending)
        return maxSum
        