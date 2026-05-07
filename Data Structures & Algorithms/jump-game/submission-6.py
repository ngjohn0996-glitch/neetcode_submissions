class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #1)goal at last_index
        goal = len(nums)-1

        #2)loop through nums[start at last_second_index]
        for curr_index in range(len(nums)-2, -1, -1):
            #2.1)if curr_index reach goal
            if curr_index + nums[curr_index] >= goal:
                #2.2)goal move to curr_index (0_index's value can be smaller)
                goal = curr_index
        
        return True if goal == 0 else False

        '''#tabulation-solution
        new_table = [False] * (len(nums))   #nums_index-reach table
        new_table[len(nums)-1] = True

        #1)start_new_table index=-2/nums_last_second_index(imagine nums_last_third_index)
        for curr_index in range(len(nums)-2, -1, -1):
        
            #2)find curr_node
            #2.1)loop through later_nums_index
            end = min(curr_index+nums[curr_index]+1, len(nums))
            for later_index in range(curr_index+1, end):
                #2.2)for curr_nums_index, check if later_nums_index reach goal
                if new_table[later_index]:
                    #2.3)find reach
                    new_table[curr_index] = True
                    break
                    
        return new_table[0]'''

