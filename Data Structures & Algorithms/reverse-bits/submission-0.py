class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        #1)loop through i(start at 0)(imagine 5)
        for i in range(32):
            
            #2)n's_bit rightmost_i_element
            rightmost_i_element = (n >> i) & 1
            #3)result's_bit leftmost_i_element
            leftmost_i_element = rightmost_i_element << (31 - i) 
            #4)prev_result's_bit  combine  result's_bit leftmost_i_element
            combine = result | leftmost_i_element
            result = combine

        return result