class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        n = len(gas)
        for start in range(n):
            found = True
            tank = 0
            for i in range(start, start + n):
                tank += gas[i % n]
                if cost[i % n] > tank:
                    found = False
                    break
                tank -= cost[i % n]
            if found:
                return start
        return -1


        