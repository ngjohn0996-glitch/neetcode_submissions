class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        prev_interval = intervals[0]
        result = 0
        
        #1)loop through intervals[start at index=1]
        for curr_interval in intervals[1:]:
            #2)if previous_interval's end smaller_than curr_interval's start
            if prev_interval[1] <= curr_interval[0]:
                #2.1)curr_interval become previous_interval, previous_interval compare with next_interval
                prev_interval = curr_interval 
            
            #2)if previous_interval is overlapping curr_interval
            else:
                #2.1)choose one_interval with smaller end
                #2.1)one_interval become previous_interval, previous_interval compare with next_interval  
                prev_interval[1] = min(prev_interval[1], curr_interval[1]) 
                result += 1
                
        return result