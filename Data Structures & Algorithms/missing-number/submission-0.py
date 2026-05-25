class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        prev_xor = 0

        #1)loop through expect, actual
        for expect in range(len(nums)):
            #2)prev_xor  bitwise_xor  expact  bitwise_xor  actual
            curr_xor = prev_xor ^ expect ^ nums[expect]
            prev_xor = curr_xor

        #3)all_expect  bitwise_xor  all_actual
        #3.1)prev_xor  bitwise_xor  final_expect
        result = prev_xor ^ len(nums)
        return result