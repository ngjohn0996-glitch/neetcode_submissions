class Solution:
    def countBits(self, n: int) -> List[int]:
        #tabulation-solution
        new_table = [0] * (n+1)   #num-number_of_1 table
        offset_index = 1

        #1)start_new_table index=1/num_01(imagine num_04)
        for curr_index in range(1, n+1):
            #2)base_index is 1, check if is every_doublize_index 
            if offset_index * 2 == curr_index:
                #2.1)curr_index become offset_index
                offset_index = curr_index
            
            #3)find curr_node
            #3.1)find (curr_index-offset_index)'s number_of_1 + 1(new_number_of_1)
            new_table[curr_index] = new_table[curr_index-offset_index] + 1

        return new_table