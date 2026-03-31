# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #3)run untill leftest_leaf_node(receive two value)
        if not root:
            return None

        #1)curr_node.left assign curr_node's right node, curr_node.right assign curr_node's left node
        left = root.left
        root.left = root.right
        root.right = left
        #2)curr_node's left node or right node run_action_#1)
        self.invertTree(root.left)
        self.invertTree(root.right)

        #4)pass curr_node to parent_call / pass final_answer  >>  continue parent_second_call, run untill DFS_last_node  
        return root

          