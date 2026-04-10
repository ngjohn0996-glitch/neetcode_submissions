class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        set_01 = set()
        dict_01 = defaultdict(list)   #node_preExeNode dict
        for node, preExeNode in prerequisites:
            dict_01[node].append(preExeNode)
        
        def dfs(node):
            #3)run untill curr_node.all_preExeNode no preExeNode
            #3)run untill curr_node.preExeNode is seen_node(no_run_action_#3.1_#3.2)
            if dict_01[node] == []:
                return True
            if node in set_01:
                return False
            

            #1)add curr_node into set
            set_01.add(node)
            #2)each_node in curr_node.preExeNode run_action_#1)
            for preExeNode in dict_01[node]:
                each_node = dfs(preExeNode) 
                if not each_node:
                    return False
            #3.1)remove curr_node from set
            set_01.remove(node)
            #3.2)curr_node no preExeNode  
            dict_01[node] = []


            #4)pass True to parent_call >> continue parent_second_call, run untill DFS_last_node
            #4)pass False to parent_call >> continue parent_call...
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True