# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path_sum = float("-inf")   #3.1)final_answer store in attribute, final_answer is two_path

    def mps(self, root):
        #4)continue parent_second_call, run untill DFS_last_node
        if not root:
            return 0

        #1)recursive case, run untill leftest_leaf_node(receive two value)
        left_node = self.mps(root.left)
        right_node = self.mps(root.right)

        #2.1)ensure path is positive_value
        leftmax = max(left_node, 0)
        rightmax = max(right_node, 0)
        #2)update max_path_sum, curr_node + left_one_path + right_one_path
        self.max_path_sum = max(self.max_path_sum, root.val+leftmax+rightmax)

        #3)pass one_path to parent_call 
        return root.val + max(leftmax, rightmax)
        

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mps(root)
        return self.max_path_sum