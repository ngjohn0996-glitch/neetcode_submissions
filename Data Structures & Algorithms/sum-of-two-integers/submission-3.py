class Solution:
    def getSum(self, a: int, b: int) -> int:
        #use 32-bit mask
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        #4)loop untill answer_02 == 0
        while b != 0:

            #1)bitwise_sum_01(1 + 0) / answer_01
            ans_01 = ( a ^ b )  &  mask
            #2)bitwise_sum_02(1 + 1) / answer_02
            ans_02 = ( (a & b) << 1 )  &  mask

            #3)answer_01  bitwise_sum_01_&_bitwise_sum_02  answer_02, on_next_loop
            a = ans_01
            b = ans_02
            
        return a if a <= max_int else ~(a ^ mask)