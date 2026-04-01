class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, list_01):
            #3)run untill last_index of list
            if index >= len(nums):
                result.append(list_01.copy())
                return


            #1)append curr_index into list
            list_01.append(nums[index])
            #2)using updated_index run_action_#1) 
            backtrack(index+1, list_01)
            #3.1)pop last/latest element
            list_01.pop()
            #4)using updated_index run_action_#1) 
            #5)index out of range of list, append into result
            backtrack(index+1, list_01)


            #6)continue parent_second_call / second_last_index, run untill all combination
        
        backtrack(0, [])
        return result