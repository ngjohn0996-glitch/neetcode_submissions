# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def __init__(self):
        self.list_01 = []   #two_fnc share same attribute

    def inorder_dfs(self, node):
        #4)run untill leftest_leaf_node(receive two value) >> continue parent_second_call, run untill DFS_last_node
        if not node:
            return None
        
        #1)recursive case, run untill leftest_node
        self.inorder_dfs(node.left)
        #2)append node.val into list
        self.list_01.append(node.val)
        #3)lefest_node's right node run_action_#1)_#2)
        self.inorder_dfs(node.right)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder_dfs(root)
        return self.list_01[k - 1]

