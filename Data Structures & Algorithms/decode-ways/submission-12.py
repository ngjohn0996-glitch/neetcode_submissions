class Solution:
    def numDecodings(self, s: str) -> int:
        '''#memorization-solution
        dict_01 = {len(s) : 1}   #num-ways dict
        
        def ways(index):
            #2)run untill last_num(imagine last_third_num)
            if index in dict_01:
                return dict_01[index]
            #2.1)#2.3)num_start_zero-0ways
            if s[index] == "0":
                return 0


            #1)find next_num 
            #2.1)find next_num's ways(plus first_element to curr_ways)
            next_num = ways(index + 1)
            next_next_num = 0
            #2.2)check if first_two_element is <=26
            if (index+1 < len(s) and ( 
                s[index] == "1" or
                s[index] == "2" and s[index+1] in "0123456")):
                #2.3)find next_next_num's ways(plus first_two_element to curr_ways)
                next_next_num = ways(index + 2)
            #3)assign curr_num-sum_ways
            dict_01[index] = next_num + next_next_num  
            

            #4)pass sum_ways to parent_call >> continue parent_second_call, run untill DFS_last_node
            return dict_01[index]

        return ways(0)'''

        #tabulation-solution
        prev_node, prev_prev_node = 1, 0

        #1)start_new_table index=1/last_num(imagine last_third_num)
        for index in range(len(s)-1, -1, -1):
            prev = prev_node
            
            #2)find curr_node
            #2.1)if curr_num_start_zero-0ways
            if s[index] == "0":
                curr_node = 0
            else:
            #2.1)find next_num's ways
                curr_node = prev_node
            #2.2)check if first_two_element is <=26
            if (index+1 < len(s) and ( 
                s[index] == "1" or
                s[index] == "2" and s[index+1] in "0123456")):
                #2.3)find next_num's ways + next_next_num's ways
                curr_node += prev_prev_node
            #3)prev_node move to next_node
            prev_node = curr_node
            #4)prev_prev_node move to next_node
            prev_prev_node = prev 

        return curr_node