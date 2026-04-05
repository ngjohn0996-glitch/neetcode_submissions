class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        
        for alphabet in word:
            if alphabet not in curr_node.children:
                curr_node.children[alphabet] = TrieNode()  
            curr_node = curr_node.children[alphabet]
            
        curr_node.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        def backtrack(node, alphabet_index):
            #3)run untill alphabet_element
            #1)curr_node
            curr_node = node
            for index in range(alphabet_index, len(word)):
                #1)curr_alphabet 
                alphabet = word[index]

                if alphabet == ".":
                    #2)TrieNode in every_curr_node.children & next_alphabet run_action_#1)
                    for trienode in curr_node.children.values():
                        every_node = backtrack(trienode, index+1)
                        if every_node:
                            return True
                    return False 
                else:
                    #3.1)check if alphabet exist in curr_node.children 
                    if alphabet not in curr_node.children:
                        return False
                    #3.2)curr_node move to TrieNode
                    curr_node = curr_node.children[alphabet]
                    
            #4)pass bool to parent_call  >>  if_False & for_loop : continue parent_second_call
            #4)self.() is not used in #3), pass bool do what?
            return curr_node.is_end_of_word

            
        return backtrack(self.root, 0)

