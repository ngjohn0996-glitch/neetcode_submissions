class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        #1)loop untill bit == 0
        while n != 0:
            #2)bit(last_element_of_bit)  bitwise_and  1
            res = n & 1
            result += res
            #3)bit right_shift by 1
            n = n >> 1
        return result