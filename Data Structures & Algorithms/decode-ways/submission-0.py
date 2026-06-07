class Solution:
    def numDecodings(self, s: str) -> int:
        # no leading zero
        # 0 can not be on its own
        # member <= 26 -> member has at most two digits
        # mapping = {chr(ord('A') + i): i+1 for i in range(26)}
        n = len(s)
        memo = defaultdict(int)
        def backtrack(idx):
            if idx == n:
                memo[idx] = 1
                return 1
            if idx in memo:
                return memo[idx]
            
            expandOne = 0
            expandTwo = 0
            if s[idx] != "0":
                expandOne = backtrack(idx+1)
                if idx <= n-2:
                    if int(s[idx:idx+2]) <= 26:
                        expandTwo = backtrack(idx+2)
            memo[idx] = expandOne + expandTwo
            return memo[idx]
        backtrack(0)
        return memo[0]
        