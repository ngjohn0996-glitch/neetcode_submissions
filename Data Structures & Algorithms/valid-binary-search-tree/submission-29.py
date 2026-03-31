# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))   #wait till valid_fnc finish
    

    def valid(self, node, floor, roof):
        #3)run untill leftest_leaf_node(receive two value) || return False
        if not node:
            return True


        #1)not(between floor and roof) >> return False
        if not(node.val > floor and node.val < roof):
            return False

        #2)curr_node's left node or right node run_action_#1)
        #2.1)go left : update_roof, use curr_floor
        left_node = self.valid(node.left, floor, node.val) 
        #2.2)go right : update_floor, use curr_roof
        right_node = self.valid(node.right, node.val, roof)

        #4)pass combine_bool to parent_call / pass final_answer  >>  continue parent_second_call, run untill DFS_last_node 
        return left_node and right_node   
        