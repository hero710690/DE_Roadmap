# A Trie structure practice
class TrieNode:
    def __init__(self):
        self.child_node =  {}
        self.word_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        for w in word:
            if w not in current_node.child_node:
                current_node.child_node[w] = TrieNode()
            
            current_node = current_node.child_node[w]
        current_node.word_end = True

    def search(self, word: str) -> bool:
        def search_in_root(node, word):
            for i, w in enumerate(word):
                if w=='.':
                    for next_node in node.child_node.values():
                        if search_in_root(next_node, word[i+1:]):
                            return True
                    return False
                    
                else:
                    if w not in node.child_node:
                        return False
                    node = node.child_node[w]
            
            return node.word_end
        return search_in_root(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)