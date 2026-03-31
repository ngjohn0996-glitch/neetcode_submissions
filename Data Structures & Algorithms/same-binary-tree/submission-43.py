# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #3)run untill leftest_leaf_node(receive two value) || return False
        if not p and not q:
            return True

        #1)if mismatch return False
        #exp: node.val is none vs node.val is 7 
        if not p or not q:
            return False
        #exp: node.val is 5 vs node.val is 7
        if p.val != q.val:
            return False     
        #2)curr_node's left node or right node run_action_#1)
        left_node = self.isSameTree(p.left, q.left)
        right_node = self.isSameTree(p.right, q.right)

        #4)pass combine_bool to parent_call / pass final_answer  >>  continue parent_second_call, run untill DFS_last_node  
        return left_node and right_node
        

        