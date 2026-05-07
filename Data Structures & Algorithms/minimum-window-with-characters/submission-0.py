class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = float("inf")
        ret = ""
        begin = end = 0
        sizeS = len(s)
        runningOcc = defaultdict(int)
        occT = defaultdict(int)
        for char in t:
            occT[char] +=1
        while end < sizeS:
            runningOcc[s[end]] += 1
            while begin <= end and isInside(runningOcc, occT):
                shortest = min(shortest, end - begin +1)
                if shortest == end - begin + 1:
                    ret = s[begin:end+1]
                runningOcc[s[begin]] -= 1
                if runningOcc[s[begin]] == 0:
                    runningOcc.pop(s[begin])
                begin +=1

            end +=1
        return ret



def isInside(occS, occT):
    for char in occT.keys():
        if occT[char] > occS.get(char, 0):
            return False
    return True
        