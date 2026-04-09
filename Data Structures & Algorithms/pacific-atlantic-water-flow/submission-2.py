class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        total_row, total_column = len(heights), len(heights[0])
        reach_pacific, reach_atlantic = set(), set()


        def dfs(row, column, reach, prev_height):
            #3)run untill next_coor not reach ocean
            if (row < 0 or row >= total_row or
                column < 0 or column >= total_column or 
                (row, column) in reach or
                heights[row][column] < prev_height):
                return
            
            #1)curr_coor reach ocean & add curr_coor into reach
            reach.add((row, column))
            #2)next_coor run_action_#1) 
            right_coor = dfs(row, column+1, reach, heights[row][column])
            left_coor = dfs(row, column-1, reach, heights[row][column])
            up_coor = dfs(row-1, column, reach, heights[row][column])
            down_coor = dfs(row+1, column, reach, heights[row][column])

            #4)continue parent_second_call, run untill all combination


        for column in range(total_column):
            dfs(0, column, reach_pacific, float("-inf"))              #first_row
            dfs(total_row-1, column, reach_atlantic, float("-inf"))   #last_row
        for row in range(total_row):
            dfs(row, 0, reach_pacific, float("-inf"))                 #first_column
            dfs(row, total_column-1, reach_atlantic, float("-inf"))   #last_column

        result = []
        for row in range(total_row):
            for column in range(total_column):
                if (row, column) in reach_pacific and (row, column) in reach_atlantic:
                    result.append((row, column))
        return result

