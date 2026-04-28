class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n

        stack = [] # (temp, index)
        for i in range(n):
            currTemp = temperatures[i]
            # for which days the currtemp is the next hotter
            while stack and currTemp > stack[-1][0]:

                temp, idx = stack.pop()
                ret[idx] = i - idx
            # find later hotter day for curr day later on
            stack.append((currTemp, i))
        return ret
            
            

        