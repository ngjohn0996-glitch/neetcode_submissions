class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        #1)loop through intervals
        for curr_interval in intervals:  
            #2)if new_interval's start larger_than curr_interval's end
            if newInterval[0] > curr_interval[1]:
                #2.1)curr_interval append into result
                result.append(curr_interval)

            #2)if new_interval's end smaller_than curr_interval's start
            elif newInterval[1] < curr_interval[0]:
                #2.1)new_interval append into result
                result.append(newInterval)
                #2.2)curr_interval become new_interval, new_interval compare with next_interval 
                newInterval = curr_interval

            #2)if new_interval is overlapping curr_interval
            else:
                #2.1)merge two_interval into new_interval, new_interval compare with next_interval 
                newInterval[0] = min(newInterval[0], curr_interval[0])
                newInterval[1] = max(newInterval[1], curr_interval[1])

        #3)after loop through all_intervals, new_interval append into result
        result.append(newInterval)
        return result

        