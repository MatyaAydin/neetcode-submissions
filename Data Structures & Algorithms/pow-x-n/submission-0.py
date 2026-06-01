class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1
        nAbs = abs(n)
        while nAbs:
            if nAbs <= 1:
                break
            nAbs -= 2
            res *= x**2

        if nAbs == 1:
            res *= x
        
        if n < 0:
            return 1 / res
        return res


        