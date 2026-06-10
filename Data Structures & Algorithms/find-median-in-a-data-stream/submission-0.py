import heapq

class MedianFinder:

    def __init__(self):
        self.size = 0
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        self.size += 1

        # Use maxHeap[0] if it exists, otherwise safely fallback to pushing to minHeap
        if self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # 2. SECOND: Balance the heaps if their sizes differ by more than 1.
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if self.size % 2 == 1:
            # Return the top of whichever heap holds the extra element
            return -self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.