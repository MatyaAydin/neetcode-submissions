class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        for idx,char in enumerate(s):
            if char == "(":
                leftStack.append(idx)
            elif char == "*":
                starStack.append(idx)
            else:
                # ")" case
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        # print(leftStack, starStack)
        while leftStack:
            par = leftStack.pop()
            if starStack:
                starIdx = starStack.pop()
                if starIdx > par:
                    continue
                else:
                    return False
            else:
                return False
        return True


        