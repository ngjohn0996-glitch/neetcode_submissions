class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum = 0
        result = float("-inf")

        #1)loop through num
        for num in nums:
            
            #2)find curr_num's sum(sum include curr_num)
            #2.1)curr_num + previous_sum 
            #2.2)curr_num (reset previous_sum)
            prev_sum = max(num+prev_sum, num)

            #3)curr_num's sum maybe is result
            result = max(result, prev_sum)    

        return result

