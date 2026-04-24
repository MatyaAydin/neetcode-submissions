class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seenNumbers = set()
        for n in nums:
            if n in seenNumbers:
                return n
            else:
                seenNumbers.add(n)
        