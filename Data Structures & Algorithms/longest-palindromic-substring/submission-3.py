class Solution:
    def longestPalindrome(self, s: str) -> str:
        result, result_len = "", float("-inf")

        #1)loop through element
        for index in range(len(s)):
            #2)two_pointer at element's left & element's right (odd_length)
            point_01, point_02 = index, index

            #3)check if palindromic  
            while (point_01 >= 0 and point_02 < len(s) and 
                   s[point_01] == s[point_02]):
                #4)update result when have longer_result_len
                if point_02-point_01+1 > result_len:
                    result = s[point_01 : point_02+1]
                    result_len = point_02 - point_01 + 1
                #4)always update two_pointer
                point_01 -= 1
                point_02 += 1


            #2)two_pointer at element & element's right (even_length)
            point_01, point_02 = index, index+1

            #3)check if palindromic 
            while (point_01 >= 0 and point_02 < len(s) and 
                   s[point_01] == s[point_02]):       
                #4)update result when have longer_result_len
                if point_02-point_01+1 > result_len:
                    result = s[point_01 : point_02+1]
                    result_len = point_02 - point_01 + 1
                #4)always update two_pointer
                point_01 -= 1
                point_02 += 1
        return result
