class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        occ = {}
        for idx, char in enumerate(s):
            if char in occ:
                start = max(start, occ[char] + 1)
            occ[char] = idx
            longest = max(longest, idx - start + 1)

        return longest