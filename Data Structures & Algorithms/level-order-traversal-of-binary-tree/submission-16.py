# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []

        while queue:
            level_list = []
            for index in range(len(queue)):
                #1)pop curr_level nodes from queue 
                node = queue.popleft()
                #3)add next_level nodes without check exist>> ensure curr_level nodes exist
                if node:
                    #2)poped_nodes add into level_list
                    level_list.append(node.val)
                    #2)poped_nodes's next_nodes add into queue
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if level_list:  #ensure level_list has element
                result.append(level_list)
        return result
        