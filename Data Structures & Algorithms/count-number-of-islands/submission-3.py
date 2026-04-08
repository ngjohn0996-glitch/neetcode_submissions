class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_column, total_row = len(grid[0]), len(grid)
        queue, set_01 = deque(), set()
        island = 0
        

        def bfs(column, row):
            queue.append((column, row))
            set_01.add((column, row))
            while queue:
                #1)pop curr_island from queue
                pop_column, pop_row = queue.popleft()

                nxt_coor = [[1,0], [-1,0], [0,-1], [0,1]]
                for diff_column, diff_row in nxt_coor:
                    new_column, new_row = pop_column+diff_column, pop_row+diff_row
                    if (new_column in range(total_column) and
                        new_row in range (total_row) and
                        grid[new_row][new_column] == "1" and
                        (new_column, new_row) not in set_01):

                        #2)add curr_island's next_coor into queue
                        queue.append((new_column, new_row))

                        #3)add curr_island's next_coor into set
                        set_01.add((new_column, new_row))


        for column in range(total_column):
            for row in range(total_row):
                if grid[row][column] == "1" and (column, row) not in set_01:
                    bfs(column, row)
                    island += 1
        return island