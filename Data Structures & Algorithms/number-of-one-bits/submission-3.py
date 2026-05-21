class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        #1)loop untill bit == 0
        while n != 0:
            #2)1 bitwise_and last_element_of_bit
            res = 1 & n
            result += res
            #3)bit right_shift by 1
            n = n >> 1
        return result