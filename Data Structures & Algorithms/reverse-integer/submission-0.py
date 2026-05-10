class Solution:
    def reverse(self, x: int) -> int:
        sgn = 1 if x >= 0 else -1
        MAXVALUE = 2**31 - 1
        MINVALUE = -2**31 

        x *= sgn
        res = 0
        while x:
            digit = x % 10
            res = 10* res + digit
            x //=10
        res *= sgn
        if res > MAXVALUE or res < MINVALUE:
            return 0
        return res
        