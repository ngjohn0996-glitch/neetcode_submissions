# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def __init__(self):
        self.combine_nodes = []
        self.index = 0

    def combine(self, root):
        #3)run untill leftest_leaf_node(receive two value) || return  >>  continue parent_second_call, run untill DFS_last_node
        if not root:
            self.combine_nodes.append("N")
            return
        
        #1)append node.val into list
        self.combine_nodes.append(str(root.val))
        #2)curr_node's left node or right node run_action_#1)
        self.combine(root.left)
        self.combine(root.right)
        
    def buildtree(self, list_01):
        #3)run untill leaf_node_index(receive two value) || return None
        if list_01[self.index] == "N":
            self.index += 1
            return None

        #1)build node
        root = TreeNode(list_01[self.index]) 
        #2)nxt_index or n_index run_action_#1)
        self.index += 1
        nxt_index = self.buildtree(list_01)
        n_index = self.buildtree(list_01)
        #3.1)run untill leaf_node_index, have_root,root.left=None,root.right=None
        root.left = nxt_index
        root.right = n_index 

        #4)pass curr_root to parent_call / pass final_answer  >>  continue parent_second_call, run untill DFS_last_node
        return root


    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.combine(root)
        return " ".join(self.combine_nodes)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        list_01 = data.split()
        return self.buildtree(list_01)
    