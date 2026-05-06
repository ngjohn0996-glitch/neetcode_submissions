class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #tabulation-solution   #text1_&_text2-common_alphabet table 
        new_table = [ [0 for i in range(len(text2)+1)] for index in range(len(text1)+1) ]    

        #1)start_new_table index=-2row/last_word of text1(imagine last_second_word of text1)
        for index in range(len(text1)-1, -1, -1):
            #1)start_new_table index=-2column/last_word of text2(imagine last_second_word of text2)
            for i in range(len(text2)-1, -1, -1): 


                #2)find curr_node
                #2.1)if text1 & text2's first_alphabet is same
                if text1[index] == text2[i]:
                    #2.2)find 1(curr_text1 & curr_text2's common_alphabet) + next_text1 & next_text2's common_alphabet
                    new_table[index][i] = 1 + new_table[index+1][i+1]


                #2.1)if text1 & text2's first_alphabet is not same
                else:   
                    #2.2)find curr_text1 & next_text2's common_alphabet  OR  next_text1 & curr_text2's common_alphabet
                    new_table[index][i] = max(new_table[index][i+1], new_table[index+1][i])

        return new_table[0][0]