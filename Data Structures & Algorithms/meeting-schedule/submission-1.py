"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda t: t.start)
        lastEnd = intervals[0].end

        for interval in intervals[1:]:
            if lastEnd > interval.start:
                return False
            lastEnd = interval.end

        return True
        
