class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        n = len(nums)

        def backtrack(curr, idx):
            if idx == n:
                solutions.append(curr[:])
                return

            curr.append(nums[idx])
            backtrack(curr, idx + 1)
            curr.pop()

            while idx + 1 < n and nums[idx] == nums[idx + 1]:
                idx += 1

            backtrack(curr, idx + 1)

        backtrack([], 0)
        return solutions

        