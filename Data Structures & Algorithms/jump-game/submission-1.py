import heapq
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if not nums[0] and n > 1:
            return False
        pq = [(0, nums[0])]
        heapq.heapify(pq)
        while pq:
            currIdx, jumpVal = heapq.heappop(pq)
            currIdx *= -1

            if currIdx + jumpVal >= n - 1:
                return True

            if jumpVal:
                for j in range(1, jumpVal + 1):
                    heapq.heappush(pq, (-(currIdx + j), nums[currIdx + j]))


        return False
        