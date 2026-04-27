class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h >= len(piles)
        # worst case: h = len(piles) -> k = max(piles)
        # k <= max(piles) = m
        #time to eat one pile of x bananas at rate k: int(x/k) + 1

        high = max(piles)
        low = 1
        lowestRate = high

        while low <= high:

            currentRate = (high + low) // 2
            currentTimeToEat = timeToEat(piles, currentRate)

            if currentTimeToEat > h:
                low = currentRate + 1
            else:
                lowestRate = currentRate
                high = currentRate - 1
        return lowestRate



def timeToEat(arr, rate):
    return sum([math.ceil(b / rate) for b in arr])
        