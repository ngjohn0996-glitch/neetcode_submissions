# final_answer >> array representation of tree / bfs include null
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #3)run untill subtree_w_onenode(receive two value) || return None
        if not preorder or not inorder:
            return None
        

        #1)find curr_root 
        root = TreeNode(preorder[0])

        #2.1)root, left_subtree, right_subtree(preoder)
        #2.1)root, left_subtree_nodes, right_subtree_nodes(preoder)
        left_subtree_nodes = inorder.index(root.val) 
        #2)left_subtree or right_subtree run_action_#1)
        left_subtree = self.buildTree(preorder[1 : left_subtree_nodes+1], inorder[:left_subtree_nodes])
        right_subtree = self.buildTree(preorder[left_subtree_nodes+1:], inorder[left_subtree_nodes+1:])

        #3.1)run untill subtree_w_onenode, have_root,root.left=None,root.right=None
        root.left = left_subtree
        root.right = right_subtree 


        #4)pass curr_root to parent_call / pass final_answer  >>  continue parent_second_call, run untill DFS_last_node 
        return root