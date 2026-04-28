class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(nums)
        def backtrack(i, currPath, runningSum):
            # print(i)
            if runningSum == target:
                # print(currPath)
                res.append(currPath[:])
                return
            if runningSum > target or i >= n:
                return

            currPath.append(nums[i])
            # if add: stay at same index because can be reused
            backtrack(i, currPath, runningSum + nums[i])
            currPath.pop()
            backtrack(i+1, currPath, runningSum)

        backtrack(0, [], 0)
        return res



        