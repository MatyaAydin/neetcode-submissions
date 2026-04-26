import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            biggest = - heapq.heappop(stones)
            secondBiggest = - heapq.heappop(stones)

            if biggest != secondBiggest:
                heapq.heappush(stones, secondBiggest - biggest)

        if len(stones) == 1:
            return - heapq.heappop(stones)
        else:
            return 0
        