class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        '''#1)loop untill bit == 0
        while n != 0:
            #2)1  bitwise_and  last_element_of_bit
            res = 1 & n
            result += res
            #3)bit right_shift by 1
            n = n >> 1
        return result'''

        #1)loop untill bit == 0
        while n != 0:   
            #2)remove rightmost 1
            #2.1)bit  bitwise_and  bit bitwise_sum two_complement_of_1
            remove = n & (n-1) 
            #3)removed_bit become bit
            n = remove
            result += 1
        return result