class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #1)goal at last_index
        goal = len(nums)-1

        #2)loop through nums[start at last_second_index]
        for curr_index in range(len(nums)-2, -1, -1):
            #2.1)if curr_index can reach goal
            if curr_index + nums[curr_index] >= goal:
                #2.2)goal move to curr_index
                goal = curr_index
        
        return True if goal == 0 else False