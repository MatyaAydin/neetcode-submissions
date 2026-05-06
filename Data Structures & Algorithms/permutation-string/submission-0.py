class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        begin = 0
        occSub = {}
        lenSub = len(s1)
        for char in s1:
            occSub[char] = occSub.get(char, 0) + 1
        occCurr = {}
        for end, char in enumerate(s2):
            occCurr[char] = occCurr.get(char, 0) + 1
            if end - begin + 1 == lenSub:
                if occCurr == occSub:
                    return True
                occCurr[s2[begin]] -= 1
                if occCurr[s2[begin]] == 0:
                    occCurr.pop(s2[begin])
                begin +=1


        return False
        