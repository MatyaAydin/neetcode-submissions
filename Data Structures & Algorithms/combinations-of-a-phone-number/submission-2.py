class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        possibilities = []
        def backtrack(word, idx):
            if idx == n:
                possibilities.append("".join(word))
                return
            for char in mapping[digits[idx]]:
                word.append(char)
                backtrack(word, idx+1)
                word.pop()

        backtrack([], 0)
        return possibilities
        