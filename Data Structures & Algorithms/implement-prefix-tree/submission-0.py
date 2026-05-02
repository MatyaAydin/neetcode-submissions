class Node:

    def __init__(self):
        self.isEndOfWord = False
        self.children = [None] * 26


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.isEndOfWord = True
                
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]

        return curr.isEndOfWord
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]

        return True
        
        