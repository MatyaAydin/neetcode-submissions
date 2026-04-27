import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = [-n for n in nums]
        heapq.heapify(nums)
        self.stream = nums
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, -val)
        tmp = []
        for _ in range(self.k):
            tmp.append(heapq.heappop(self.stream))
        val = -tmp[-1]
        for i in range(self.k):
            heapq.heappush(self.stream, tmp[i])
        return val
        

        
