class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1

        #1)loop through top to middle
        while top < bottom:
            #2)loop through left to second_right
            for index in range(right - left):   #move one_step at top_or_middle
                
                #3)at left
                #3)top left become bottom left
                #3)bottom left become bottom right
                #3)bottom right become top right
                #3)top right become top left

                #4)at north
                north_element = matrix[top][left + index]
                #4)north's element become west's element
                matrix[top][left + index] = matrix[bottom - index][left]
                #4)west's element become south's element
                matrix[bottom - index][left] = matrix[bottom][right - index]
                #4)south's element become east's element
                matrix[bottom][right - index] = matrix[top + index][right]
                #4)east's element become north's element
                matrix[top + index][right] = north_element

            top += 1
            bottom -= 1
            left += 1
            right -= 1    