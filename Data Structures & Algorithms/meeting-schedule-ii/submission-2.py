"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        curr_start = sorted([interval.start for interval in intervals])  
        curr_end = sorted([interval.end for interval in intervals])
        start_index, end_index = 0, 0
        room, max_rooms = 0, 0

        #1)curr_start, curr_end[start at first_end]
        while start_index < len(curr_start):

            #2)if curr_start smaller than curr_end
            if curr_start[start_index] < curr_end[end_index]:
                #2.1)interval+1 / overlapping_interval+1
                room += 1
                #2.2)curr_start move to next_start(count untill all overlapping_interval at curr_end)
                start_index += 1
                max_rooms = max(max_rooms, room)

            #3)if curr_start larger_than curr_end(two_interval align)
            else:
                #3.1)curr_end move to next_end(find all overlapping_interval at curr_end) 
                end_index += 1 
                #3.2)interval-1 / overlapping_interval-1
                #3.2)next_end count curr_start's interval instead curr_end's interval
                room -= 1
        return max_rooms