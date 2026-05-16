class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1

        #1)loop through layers
        while top < bottom and left < right:
            #2)loop through left to second_right
            for index in range(right - left):   #on each_layer, move_one_step from left to second_right
                
                #3)at top left
                #3)top left become bottom left
                #3)bottom left become bottom right
                #3)bottom right become top right
                #3)top right become top left

                #4)at point_01
                north_element = matrix[top][left + index]
                #4)point_01 loop through left to second_right 
                matrix[top][left + index] = matrix[bottom - index][left]
                #4)point_02 loop through bottom to second_top
                matrix[bottom - index][left] = matrix[bottom][right - index]
                #4)point_03 loop through right to second_left
                matrix[bottom][right - index] = matrix[top + index][right]
                #4)point_04 loop through top to second_bottom
                matrix[top + index][right] = north_element

            top += 1
            bottom -= 1
            left += 1
            right -= 1    