class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n

        for i in range(n):
            currTemp = temperatures[i]
            ahead = 0
            while i + ahead < n:
                if temperatures[i+ahead] > currTemp:
                    ret[i] = ahead
                    break
                ahead +=1
        return ret
        