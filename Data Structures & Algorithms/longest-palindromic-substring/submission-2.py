class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest = 0
        n = len(s)
        for center in range(n):
            #odd length
            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:
                # in this loop we are sure that s[left:right+1] is a palindrom
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right +=1

            left = center
            right = center + 1
            # even length
            while left >= 0 and right < n and s[left] == s[right]:
                # in this loop we are sure that s[left:right+1] is a palindrom
                if right - left + 1 > longest:
                    longest = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right +=1
        return res


        