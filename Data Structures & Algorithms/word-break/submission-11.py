class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #tabulation-solution
        new_table = [False] * (len(s)+1)   #s_index-match table
        new_table[len(s)] = True

        #1)start_new_table index=-2/s_last_index(imagine s_1stmatch_index)
        for curr_index in range(len(s)-1, -1, -1):

            #2)find curr_node
            #2.1)loop through word
            for word in wordDict:
                #2.2)at curr_s_index, check if match word 
                if (curr_index+len(word) <= len(s) and
                    s[curr_index : curr_index+len(word)] == word):
                    #2.3)find later_s_index's match
                    new_table[curr_index] = new_table[curr_index+len(word)]  
                #2.3)find untill later_s_index's match is True
                if new_table[curr_index]:
                    break
            
        return new_table[0]      