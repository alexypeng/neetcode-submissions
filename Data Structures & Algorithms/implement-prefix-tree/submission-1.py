class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.node
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.node
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for letter in prefix:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        return True
                
        