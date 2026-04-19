class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sequ_lengths = {}
        lookup = set(nums)
        max_sequ_length = 0

        for n in nums:
            # beginning of a sequence:
            if n-1 not in lookup:
                curr_length = 0
                curr_number = n
                while curr_number in lookup:
                    curr_length += 1
                    curr_number += 1
                max_sequ_length = max(max_sequ_length, curr_length)

        return max_sequ_length