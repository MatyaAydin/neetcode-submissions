import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k largest -> maintain min heap, when length exceeds, remove
        minHeap = []
        heapq.heapify(minHeap)
        for n in nums:
            # print(minHeap)
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]       