from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        mapping = {
            "(": ")",
            "{": "}",
            "[":"]"
        }
        for c in s:

            if c in mapping:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    curr_open_bracket = stack.pop()
                    if c != mapping[curr_open_bracket]:
                        return False
        return not stack


        