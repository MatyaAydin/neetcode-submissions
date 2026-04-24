class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for idx, n in enumerate(nums):
            if nums[abs(nums[idx]) - 1] < 0:
                return abs(n)
            nums[abs(nums[idx]) - 1] *= -1

        