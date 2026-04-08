"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict_01 = {}
        
        def dfs(node):
            #3)run untill curr_node.neighbors have copy_node
            if node in dict_01:
                return dict_01[node] 


            #1)create curr_node_copy
            copy_node = Node(node.val)
            dict_01[node] = copy_node
            #2)each node in curr_node.neighbors run_action_#1)  
            for neighbors in node.neighbors:
                each_node = dfs(neighbors)
                #3.1)curr_node_copy.children assign curr_node.neighbor's copy_node  
                copy_node.neighbors.append(each_node)


            #4)pass curr_node_copy to parent_call  >>  continue parent_second_call, run untill DFS_last_node
            return copy_node

        return dfs(node) if node else None 