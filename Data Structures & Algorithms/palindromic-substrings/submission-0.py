class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for center in range(n):
            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:
                count +=1
                left -=1
                right +=1
            left = center
            right = center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count +=1
                left -=1
                right +=1
        return count
        