import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # nums = [-n for n in nums]
        heapq.heapify(nums)
        self.stream = nums
        self.k = k
        while len(self.stream) > k:
            heapq.heappop(self.stream)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        if len(self.stream) > self.k:
            val = heapq.heappop(self.stream)
        return self.stream[0]
     

        
