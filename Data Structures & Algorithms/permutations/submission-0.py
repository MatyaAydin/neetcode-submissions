class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)

        def backtrack(curr, chosen):
            if len(curr) == n:
                permutations.append(curr[:])
            for i in range(n):
                if not chosen[i]:
                    curr.append(nums[i])
                    chosen[i] = True
                    backtrack(curr, chosen)
                    curr.pop()
                    chosen[i] = False

        backtrack([], [False] * n)
        return permutations
            


        