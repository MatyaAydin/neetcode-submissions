class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        nCoins = len(coins)
        memo = defaultdict(int)

        def backtrack(currAmount, idx):
            tup = (currAmount,idx)
            if tup in memo:
                return memo[tup]
            if currAmount == 0:
                memo[tup] = 1
                return memo[tup]
            if idx == nCoins or currAmount < 0:
                memo[tup] = 0
                return memo[tup]

            useSame = backtrack(currAmount - coins[idx], idx)
            goNext = backtrack(currAmount, idx + 1)
            memo[tup] = useSame + goNext
            return memo[tup]

        backtrack(amount, 0)
        return memo[(amount, 0)]

        