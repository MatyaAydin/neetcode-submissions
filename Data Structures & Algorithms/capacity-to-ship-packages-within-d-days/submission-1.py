class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # max(weights) <= capacity <= sum(weights)

        low = max(weights)
        high = sum(weights)
        n = len(weights)

        while low <= high:

            capacity = (low + high) // 2
            daysTaken = evalDays(weights, capacity)

            if daysTaken <= days:
                high = capacity - 1
            else: # daystaken > days
                low = capacity + 1
        return low
            


def evalDays(weights, capacity):
    load = 0
    daysTaken = 1
    for w in weights:
        load += w
        if load > capacity:
            daysTaken += 1
            load = w
    return daysTaken