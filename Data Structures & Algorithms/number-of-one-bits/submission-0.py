class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        #1)loop untill bit == 0
        while n > 0:
            #2)check if last_element of bit is 1
            res = n & 1
            result += res
            #3)bit right_shift by 1
            n = n >> 1
        return result