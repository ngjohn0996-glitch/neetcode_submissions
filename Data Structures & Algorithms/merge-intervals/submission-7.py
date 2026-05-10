class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        result = [intervals[0]]

        #1)loop through intervals[start at index=1]
        for curr_interval_start, curr_interval_end in intervals[1:]:
            prev_interval = result[-1]

            #2)if previous_interval's end smaller_than curr_interval's start
            if prev_interval[1] < curr_interval_start:
                #2.1)curr_interval append into result
                result.append([curr_interval_start, curr_interval_end])
                #2.2)curr_interval become previous_interval, previous_interval compare with next_interval

            #2)if previous_interval is overlapping curr_interval
            else:
                #2.1)merge two_interval into previous_interval, previous_interval compare with next_interval
                prev_interval[1] = max(prev_interval[1], curr_interval_end)

        return result