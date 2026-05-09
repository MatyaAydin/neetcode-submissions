class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid = []
        def backtrack(curr, left, right):
            if len(curr) == 2*n:
                valid.append("".join(curr))
                return

            if left < n:
                if right <= left:
                    curr.append("(")
                    left +=1
                    backtrack(curr, left, right)
                    curr.pop()
                    left -=1
            if right < n:
                if right <= left:
                    curr.append(")")
                    right +=1
                    backtrack(curr, left, right)
                    curr.pop()
                    right -= 1

        backtrack([], 0, 0)
        return valid
        