class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #tabulation-solution
        new_table = [1] * (len(nums))   #nums_index-ascending table

        #1)start_new_table index=-1/nums_last_index(imagine nums_last_third_index)
        for curr_index in range(len(nums)-1, -1, -1):
        
            #2)find curr_node
            #2.1)loop through later_nums_index
            for later_index in range(curr_index+1, len(nums)):
                #2.2)check if curr_nums_index is smaller than later_nums_index
                if nums[curr_index] < nums[later_index]:
                    #2.2)find 1(curr_nums_index) + later_nums_index's ascending  
                    new_table[curr_index] = max(new_table[curr_index], 1 + new_table[later_index])

        return max(new_table)