class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        set_01 = set()
        total_column, total_row = len(board[0]), len(board)
        
        def backtrack(index, column, row):
            #3)run untill last_element || last_element_possible (return all False)
            if index == len(word):
                return True
            if (column < 0 or column >= total_column or 
                row < 0 or row >= total_row or
                word[index] != board[row][column] or
                (column, row) in set_01):
                return False


            #1)append curr_coor into set
            set_01.add((column, row))
            #2)next_coor run_action_#1) 
            right_coor = backtrack(index+1, column+1, row)
            left_coor = backtrack(index+1, column-1, row)
            up_coor = backtrack(index+1, column, row-1)
            down_coor = backtrack(index+1, column, row+1) 
            #3.1)remove from set
            set_01.remove((column, row)) 


            #4)pass combine_bool to parent_call  >>  continue parent_second_call, run untill all combination
            return right_coor or left_coor or up_coor or down_coor

        for column in range(total_column):
            for row in range(total_row):
                 if backtrack(0, column, row):
                    return True
        return False
            