class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max_product, prev_min_product = 1, 1   #-ve_num * prev_min_product >> max_product
        result = float("-inf")

        #1)loop through num
        for num in nums:

            #2)find curr_num's max_product(product include curr_num)
            #3)find curr_num's min_product(product include curr_num)
            #2.1)#3.1)curr_num * previous_max_product  ||  curr_num * previous_min_product
            #2.2)#3.1)curr_num (reset previous_product)
            max_product = num*prev_max_product
            min_product = num*prev_min_product 
  
            prev_max_product = max(max_product, min_product, num)
            prev_min_product = min(max_product, min_product, num)
            
            #3)curr_num's max_product maybe is result
            result = max(result, prev_max_product)

        return result

