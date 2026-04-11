class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        set_01 = set()
        dict_01 = defaultdict(list)   #node_neighborNode dict
        for node1, node2 in edges:
            dict_01[node1].append(node2)
            dict_01[node2].append(node1)
        
        def dfs(node, prev_node):
            #3)run untill parent_leaf_node.all_neighborNode not seen_node
            #3)run untill curr_node.neighborNode is seen_node
            if node in set_01:
                return False


            #1)add curr_node into set
            set_01.add(node)
            #2)each_node in curr_node.neighborNode run_action_#1)
            for neighbors in dict_01[node]:
                if neighbors == prev_node:   #2)except prev_node
                    continue
                each_node = dfs(neighbors, node)
                if not each_node:
                    return False


            #4)pass True to parent_call >> continue parent_second_call, run untill DFS_last_node
            #4)pass False to parent_call >> continue parent_call...
            return True

        return dfs(0, float("inf")) and n == len(set_01)