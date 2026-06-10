import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = [0] * 26
        lastRan = deque()
        pq = []
        for t in tasks:
            counter[ord(t) - ord('A')] += 1
        for i in range(26):
            if counter[i]:
                heapq.heappush(pq, (-counter[i], chr(i + ord('A'))))

        while pq or lastRan:
            time += 1
            
            if pq:
                freq, curr = heapq.heappop(pq)
                freq *= -1
                freq -= 1 # executed
                if freq > 0:
                    lastRan.append((-freq, curr, time + n))
            
            # if the task at the front of the queue is done cooling down, put it back in the heap
            if lastRan and lastRan[0][2] == time:
                ready_freq, ready_task, _ = lastRan.popleft()
                heapq.heappush(pq, (ready_freq, ready_task))
 
        return time