"""
LeetCode 211

"""
class Node:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.next = dict()


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str):

        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if not cur.next.get(c):
                cur.next[c] = Node(False)
            cur = cur.next[c]

        if not cur.is_word:
            cur.is_word = True

    def search(self, word: str) -> bool:
        return self.match(self.root, word, 0)

    def match(self, node: Node, word: str, index: int) -> bool:
        if index == len(word):
            return node.is_word

        c = word[index]
        if not c == '.':
            if not node.next.get(c):
                return False
            return self.match(node.next.get(c), word, index+1)
        else:
            for nextChar in node.next.keys():
                if self.match(node.next.get(nextChar), word, index + 1):
                    return True
            return False
