class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while high >= low:
            mid = (high + low) // 2
            curr = nums[mid]

            if curr == target:
                return mid
            elif curr > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

        