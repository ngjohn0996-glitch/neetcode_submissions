class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #tabulation-solution
        new_table = [False] * (len(s)+1)   #s_index-match table
        new_table[len(s)] = True

        #1)start_new_table index=-2/s_last_index(imagine first_match_index)
        for index in range(len(s)-1, -1, -1):

            #2)find curr_node
            #2.1)loop through word
            for word in wordDict:
                #2.2)check if word match at curr_index 
                if (index+len(word) <= len(s) and
                    word == s[index : index+len(word)]):
                    #2.3)find later_index's match
                    new_table[index] = new_table[index+len(word)]  
                if new_table[index]:
                    break
            
        return new_table[0]      