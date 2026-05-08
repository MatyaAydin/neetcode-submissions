import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        begin = 0
        end = k-1
        n = len(nums)
        pq = []
        maximums = []
        for i in range(k-1):
            pq.append((-nums[i], i))
        heapq.heapify(pq)
        while end < n:
            heapq.heappush(pq, (-nums[end], end))
            while pq:
                data, idx = heapq.heappop(pq)
                if idx < begin:
                    continue
                maximums.append(-data)
                heapq.heappush(pq, (data, idx))
                break
            begin +=1
            end +=1

        return maximums

        