# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #3)continue parent_second_call, run untill DFS_last_node
        if not root:
            return 0

        #1)recursive case, run untill leftest_leaf_node(receive two value)
        left_node = self.maxDepth(root.left)
        right_node = self.maxDepth(root.right)
        
        #2)pass #2.1) to parent_call / pass final_answer   
        #2.1)curr_node as 1, plus bigger_depth of left node or right node   
        return 1 + max(left_node, right_node)  

        '''if not root:
            return 0


        queue = deque([root])
        level = 0

        while queue:
            #1)loop through curr_level nodes
            for index in range(len(queue)):
                #1.1)pop curr_level nodes from queue 
                node = queue.popleft()
                #1.2)ensure next_level nodes exist
                #1.2)add next_level nodes into queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level'''

        '''stack = [[root,1]]
        max_level = 0

        while stack:
            #1)pop curr_level nodes from stack
            node, level = stack.pop()
            #3)add next_level nodes without check exist>> ensure curr_level nodes exist
            if node:
                #2)add next_level nodes into stack
                stack.append([node.right, level+1])
                stack.append([node.left, level+1])
                max_level = max(max_level, level)
        return max_level'''

