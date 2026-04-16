class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dict_01 = {alphabet : set()   for word in words for alphabet in word}

        #1)loop through every_two_word
        for index in range(len(words)-1):
            word1, word2 = words[index], words[index+1]
            word_length = min(len(word1), len(word2))
            #edge_case
            if word1[0:word_length] == word2[0:word_length] and len(word1) > len(word2):
                return ""
            #2)loop through alphabet
            for i in range(word_length):
                #3)first_different_alphabet add into dict_01, {alphabet : after_alphabet}
                if word1[i] != word2[i]:
                    dict_01[word1[i]].add(word2[i])
                    break



        dict_02 = {}   #True=seen_node, False=node already in result
        result = []

        def dfs(node):
            #3)run untill leaf_node not seen_node
            #3)run untill curr_node.neighborNode is seen_node(no_run_action_#3.1_#3.2)
            if node in dict_02:
                return dict_02[node]


            #1)assign curr_node-True
            dict_02[node] = True
            #2)each_node in curr_node.neighborNode run_action_#1)
            for neighbors in dict_01[node]:
                each_node = dfs(neighbors)
                if each_node:
                    return True
            #3.1)assign curr_node-False
            dict_02[node] = False
            #3.2)append into result
            result.append(node)


            #4)continue parent_second_call, run untill DFS_last_node
            #4)pass True to parent_call >> continue parent_call...

        for node in dict_01:
            if dfs(node):
                return ""
        result.reverse()
        return "".join(result)