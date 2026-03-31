# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #1.1)run untill leaf_node(receive one value)
        if not root:
            return None

        #1)recursive case, run untill leaf_node || return curr_node 
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)

        #2)XX pass value to previous_call
        #2)return self.lowestCommonAncestor() >> pass value/curr_node as final_answer  
        else:
            return root