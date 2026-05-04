class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #tabulation-solution
        newtable_bottom_row = [1] * n   #grid_index-ways table
    
        #1)start_new_table index=-2row/grid_index_last_second_row
        for index in range(m-1):
            newtable_curr_row = [1] * n
            #1)start_new_table index=-2column/grid_index_last_second_column(imagine grid_index_last_third_column)
            for i in range(n-2, -1, -1):
                
                #2)find curr_node
                #2.1)find right_grid_index's ways + bottom_grid_index's ways
                newtable_curr_row[i] = newtable_curr_row[i+1] + newtable_bottom_row[i]

            #3)after loop_through all_column, curr_row move to upper_row
            #3)after loop_through all_column, bottom_row move to upper_row
            newtable_bottom_row = newtable_curr_row 

        return newtable_bottom_row[0] 