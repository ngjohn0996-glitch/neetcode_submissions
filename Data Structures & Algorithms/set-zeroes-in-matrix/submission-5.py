class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, columns = len(matrix), len(matrix[0]) 
        row_index_zero = False   
        #column_index-turn_zero table   #row_index-turn_zero table

        #1)loop through rows
        for curr_row_index in range(rows):
            #1)loop through columns
            for curr_column_index in range(columns):
                #2)check if grid_index is zero
                if matrix[curr_row_index][curr_column_index] == 0:
                    #3)column_index table's  curr_column_index find turn_zero
                    matrix[0][curr_column_index] = 0
                    #3)row_index table's  curr_row_index find turn_zero
                    if curr_row_index > 0:
                        matrix[curr_row_index][0] = 0
                    else:
                        row_index_zero = True


        #4)loop through rows(start at second_row)
        for curr_row_index in range(1, rows):
            #4)loop through columns(start at second_column)
            for curr_column_index in range(1, columns):
                #5)check if column_index table's  curr_column_index is turn_zero OR row_index table's  curr_row_index is turn_zero
                if matrix[0][curr_column_index] == 0 or matrix[curr_row_index][0] == 0:
                    #6)grid_index turn zero
                    matrix[curr_row_index][curr_column_index] = 0

        #7)column_index_zero turn_zero
        if matrix[0][0] == 0:
            for index in range(rows):
                matrix[index][0] = 0
        #8)row_index_zero turn_zero
        if row_index_zero:
            for index in range(columns):
                matrix[0][index] = 0

