class Solution:
    def climbStairs(self, n: int) -> int:
        '''#memorization-solution
        dict_01 = {1 : 1, 2 : 2}   #stair-ways dict

        def ways(n):
            if n in dict_01:
                #2)run untill stair=3
                return dict_01[n]


            else:
                #1)find prev_stair
                #2.1)find prev_stair's ways & prev_prev_stair's ways (plus 1/2 step to curr_stair) (prev_prev_prev_stair >> overlap_w_prev_stair/prev_prev_stair)
                prev_stair = ways(n - 1)
                prev_prev_stair = ways(n - 2)
                #3)assign curr_stair-sum_ways 
                dict_01[n] = prev_stair + prev_prev_stair 


                #4)pass sum_ways to parent_call >> continue parent_second_call, run untill DFS_last_node
                return dict_01[n] 

        return ways(n)'''

        #edge-case
        if n == 0:
            return 1
        if n == 1:
            return 1
        #tabulation-solution
        prev_node, prev_prev_node = 1, 1

        #1)start_new_table stair/index=2
        for index in range(2, n+1):
            prev = prev_node   #4.1)before prev_node assign prev_node.next, prev_node is prev_node
            
            #2)find curr_node
            curr_node = prev_node + prev_prev_node 
            #3)prev_node move to next_node
            prev_node = curr_node
            #4)prev_prev_node move to next_node
            prev_prev_node = prev 

        return curr_node

