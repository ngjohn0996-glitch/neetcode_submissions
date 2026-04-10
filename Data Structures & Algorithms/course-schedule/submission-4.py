class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        set_01 = set()
        dict_01 = defaultdict(list)   #node_neighbors dict
        for node, neighbors in prerequisites:
            dict_01[node].append(neighbors)
        
        def dfs(node):
            #3)run untill curr_node.neighbors no neighbors
            #3)run untill curr_node.neighbors is seen_node(no_run_action_#3.1)) 
            if node in set_01:
                return False
            if dict_01[node] == []:
                return True
            


            #1)add curr_node into set
            set_01.add(node)
            #2)each node in curr_node.neighbors run_action_#1)
            for neighbors in dict_01[node]:
                each_node = dfs(neighbors) 
                if not each_node:
                    return False
            #3.1)remove from set
            set_01.remove(node)


            #4)pass True to parent_call >> continue parent_second_call, run untill DFS_last_node
            #4)pass False to parent_call >> continue parent_call...
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True