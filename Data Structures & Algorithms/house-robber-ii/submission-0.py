class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge-case
        if len(nums) == 1:
            return nums[0]
            
        #1)list_houses not_include_first_house's total_money  VS  list_houses not_include_last_house's total_money
        return max(self.total_money(nums[1:]), self.total_money(nums[:-1]))


    def total_money(self, list_houses):
        prev_node, prev_prev_node = 0, 0

        for num in list_houses:
            prev = prev_node

            curr_node = max(prev_node, num+prev_prev_node)
            prev_node = curr_node
            prev_prev_node = prev
                
        return curr_node

