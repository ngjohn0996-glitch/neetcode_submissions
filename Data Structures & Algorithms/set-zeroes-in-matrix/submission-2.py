class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, columns = len(matrix), len(matrix[0]) 
        zero_index_row = False   
        #index_column-turn_zero table   #index_row-turn_zero table

        #1)loop through rows
        for curr_index_row in range(rows):
            #1)loop through columns
            for curr_index_column in range(columns):
                #2)check if grid_index is zero
                if matrix[curr_index_row][curr_index_column] == 0:
                    #3)index_column table's  curr_index_column find turn_zero
                    matrix[0][curr_index_column] = 0
                    #3)index_row table's  curr_index_row find turn_zero
                    if curr_index_row > 0:
                        matrix[curr_index_row][0] = 0
                    else:
                        zero_index_row = True


        #1)loop through rows(start at second_row)
        for curr_index_row in range(1, rows):
            #1)loop through columns(start at second_column)
            for curr_index_column in range(1, columns):
                #2)check if index_column table's  curr_index_column is turn_zero OR index_row table's  curr_index_row is turn_zero
                if matrix[0][curr_index_column] == 0 or matrix[curr_index_row][0] == 0:
                    #3)curr_grid_index turn zero
                    matrix[curr_index_row][curr_index_column] = 0

        #4)zero_index_column turn_zero
        if matrix[0][0] == 0:
            for index in range(rows):
                matrix[index][0] = 0
        #5)zero_index_row turn_zero
        if zero_index_row:
            for index in range(columns):
                matrix[0][index] = 0

