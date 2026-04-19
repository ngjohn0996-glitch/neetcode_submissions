class Solution:
    def climbStairs(self, n: int) -> int:
        #memorization-solution
        dict_01 = {1 : 1, 2 : 2}   #stair-ways dict

        def ways(n):
            if n in dict_01:
                #2)run untill stair=3
                return dict_01[n]


            else:
                #1)find prev_stair
                #2.1)find prev_stair's ways & prev_prev_stair's ways (plus 1/2 step to curr_stair) 
                prev_stair = ways(n - 1)
                prev_prev_stair = ways(n - 2)
                #3)assign curr_stair-sum_ways 
                dict_01[n] = prev_stair + prev_prev_stair 


                #4)pass sum_ways to parent_call >> continue parent_second_call, run untill DFS_last_node
                return dict_01[n] 

        return ways(n)