class Solution:
    def rob(self, nums: List[int]) -> int:
        #tabulation-solution
        prev_node, prev_prev_node = 0, 0

        #1)start_new_table index=1/first_house(imagine fifth_house)
        for num in nums:
            prev = prev_node

            #2)find curr_node(prev_house's total_money OR curr_house's money + prev_prev_house's total_money)
            curr_node = max(prev_node, num+prev_prev_node)
            #3)prev_node move to next_node
            prev_node = curr_node
            #4)prev_prev_node move to next_node
            prev_prev_node = prev
            
        return curr_node

        