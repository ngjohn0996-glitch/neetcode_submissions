class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr_node = self.root
        for alphabet in word:
            if alphabet not in curr_node.children:
                curr_node.children[alphabet] = TrieNode()  
            curr_node = curr_node.children[alphabet] 
        curr_node.is_end_of_word = True
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWord(word)
            
        result, set_01 = set(), set()
        total_column, total_row = len(board[0]), len(board)
        
        
        def backtrack(curr_node, column, row, string):
            #3)run untill TrieNode.children no next_coor's alphabet
            if (column < 0 or column >= total_column or 
                row < 0 or row >= total_row or
                (column, row) in set_01 or
                board[row][column] not in curr_node.children):
                return

            #1)curr_alphabet exist in curr_node.children & curr_node move to TrieNode
            curr_node = curr_node.children[board[row][column]]
            #1)check if TrieNode is_end_of_word
            string += board[row][column]
            if curr_node.is_end_of_word:
                result.add(string)
            #1)append curr_coor into set
            set_01.add((column, row))
                
            #2)next_coor run_action_#1) 
            right_coor = backtrack(curr_node, column+1, row, string)
            left_coor = backtrack(curr_node, column-1, row, string)
            up_coor = backtrack(curr_node, column, row-1, string)
            down_coor = backtrack(curr_node, column, row+1, string) 
            
            #3.1)remove from set
            set_01.remove((column, row)) 

            #4)continue parent_second_call, run untill all combination


        for column in range(total_column):
            for row in range(total_row):
                backtrack(self.root, column, row, "")
                    
        return list(result)