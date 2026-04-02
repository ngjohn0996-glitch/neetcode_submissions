class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #1)curr_node
        curr_node = self.root
        
        #2)loop through alphabet 
        for alphabet in word:
            #2.1)curr_node.children assign alphabet-TrieNode
            if alphabet not in curr_node.children:
                curr_node.children[alphabet] = TrieNode()  
            #2.2)curr_node move to TrieNode
            curr_node = curr_node.children[alphabet]
        #3)last alphabet.is_end_of_word assign True
        curr_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        #1)curr_node
        curr_node = self.root

        #2)loop through alphabet 
        for alphabet in word:
            #2.1)check if alphabet exist in curr_node.children 
            if alphabet not in curr_node.children:
                return False
            #2.2)curr_node move to TrieNode
            curr_node = curr_node.children[alphabet]
        #3)at last alphabet check if word exist
        return curr_node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        #1)curr_node
        curr_node = self.root

        #2)loop through alphabet 
        for alphabet in prefix:
            #2.1)check if alphabet exist in curr_node.children 
            if alphabet not in curr_node.children:
                return False
            #2.2)curr_node move to TrieNode
            curr_node = curr_node.children[alphabet]
        #3)at last alphabet no need check if word exist
        return True
        
