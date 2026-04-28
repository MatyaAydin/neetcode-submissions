class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        n = len(nums)
        def backtrack(i, subset):
            if i == n:
                allSubsets.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            backtrack(i+1, subset)

        backtrack(0, [])
        return allSubsets
        