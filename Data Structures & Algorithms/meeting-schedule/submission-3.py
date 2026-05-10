"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #edge-case
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda x : x.start)
        prev_interval = intervals[0]
        #1)loop through intervals[start at index=1]
        for curr_interval in intervals[1:]:

            #2)check if previous_interval's end larger_than curr_interval's start
            if prev_interval.end > curr_interval.start:
                #2.1)break loop
                return False

            #3)curr_interval become previous_interval, previous_interval compare with next_interval
            prev_interval = curr_interval
            
        return True