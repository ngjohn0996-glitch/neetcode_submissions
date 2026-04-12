class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [index for index in range(n)]   #each_node's parent
        size = [1] * n   #each_node's size

        def find_root(node):
            curr_node = node
            #1)curr_node not rootNode
            while curr_node != parent[curr_node]:
                #2)curr_node become parent_node
                parent[curr_node] = parent[parent[curr_node]]   #2)path halving, curr_node become grandparent_node
                curr_node = parent[curr_node]
            return curr_node
        
        def union(node1, node2):
            rootNode01, rootNode02 = find_root(node1), find_root(node2) 
            #1)ensure two_rootNode
            if rootNode01 == rootNode02:
                return 0
            #2)rootNode_w_smallersize.parent is rootNode_w_biggersize
            if size[rootNode01] < size[rootNode02]:
                parent[rootNode01] = rootNode02
                size[rootNode02] += size[rootNode01]
            else:
                parent[rootNode02] = rootNode01
                size[rootNode01] += size[rootNode02]
            #3)union success, total_individual-1 
            return 1
        
        total_individual = n
        for node1, node2 in edges:
            total_individual -= union(node1, node2)
        return total_individual

