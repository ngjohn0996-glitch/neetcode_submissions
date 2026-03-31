class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, list_01, total):
            #3)run untill combination_lack_one_element to total > target || total == target 
            if total > target:
                return 
            if total == target:
                result.append(list_01.copy())
                return
            #5)run untill index out_of_range
            if index >= len(nums):
                return
            

            #1)append zero_index into list
            list_01.append(nums[index])
            #2)using same_index run_action_#1)
            backtrack(index, list_01, total + nums[index])
            #3.1)pop last/latest element
            list_01.pop()  
            #4)using updated_index run_action_#1) 
            backtrack(index+1, list_01, total)


            #6)continue parent_second_call, run untill all combination
        
        backtrack(0, [], 0)
        return result

        