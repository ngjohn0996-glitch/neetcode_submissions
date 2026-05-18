class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        result = []

        #1)loop through layers
        while top < bottom and left < right:
            #2)loop through left_to_right at_top
            for index in range(left, right):
                result.append(matrix[top][index])
            top += 1

            #3)loop through top_to_bottom at_right
            for index in range(top, bottom):
                result.append(matrix[index][right-1]) 
            right -= 1

            if top < bottom:   #if_action_#3) dont_run, duplicate right
                #4)loop through right_to_left at_bottom
                for index in range(right-1, left-1, -1):
                    result.append(matrix[bottom-1][index])
                bottom -= 1

            if left < right:   #if_action_#4) dont_run, duplicate bottom
                #5)loop through bottom_to_up at_left
                for index in range(bottom-1, top-1, -1):
                    result.append(matrix[index][left])
                left += 1
        return result