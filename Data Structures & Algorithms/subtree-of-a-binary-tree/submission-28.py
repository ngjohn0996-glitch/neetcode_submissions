# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #3)run untill leftest_leaf_node(receive two value) || return True
        if not root and subRoot:
            return False 

        #1)if match return True
        if self.isSameTree(root,subRoot):
            return True
        #2)curr_node's left node or right node run_action_#1)
        left_node = self.isSubtree(root.left, subRoot)
        right_node = self.isSubtree(root.right, subRoot)

        #4)pass combine_bool to parent_call / pass final_answer  >>  continue parent_second_call, run untill DFS_last_node 
        return left_node or right_node 

    def isSameTree(self, p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False
            if p.val != q.val:
                return False     
            left_node = self.isSameTree(p.left, q.left)
            right_node = self.isSameTree(p.right, q.right)

            return left_node and right_node 
            