class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        #1)loop untill n's_bit == 0
        while n != 0:
            #2)check if curr_bit's last_element is 1
            #2.1)curr_bit  bitwise_and  1's_bit
            res = n & 1
            result += res
            #3)curr_bit right_shift by 1
            n = n >> 1
        return result

        '''#1)loop untill n's_bit == 0
        while n != 0:   
            #2)curr_bit's rightmost_1 need_remove
            #2.1)curr_bit  bitwise_and  (curr_bit bitwise_minus 1's_bit) 
            remove = n & (n-1) 
            #3)removed_bit become curr_bit
            n = remove
            result += 1
        return result'''