class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for num in nums:
            if num in dict:   #2)check key existance
                return True
            dict [num] = "value"   #1)loop through and assign key-value
        return False
        