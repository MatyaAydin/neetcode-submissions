class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda i: i[0])
        merged = []
        minElem = intervals[0][0]
        maxElem = intervals[0][1]
        for interval in intervals[1:]:
            if minElem <= interval[0] <= maxElem:
                maxElem = max(interval[1], maxElem)
            else:
                merged.append([minElem, maxElem])
                minElem = interval[0]
                maxElem = interval[1]
        merged.append([minElem, maxElem])
        return merged        