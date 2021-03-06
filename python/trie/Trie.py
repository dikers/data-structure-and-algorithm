"""
LeetCode 208

"""
class Node:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.next = dict()


class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, word: str):
        
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if not cur.next.get(c):
                cur.next[c] = Node(False)
            cur = cur.next[c]

        if not cur.is_word:
            cur.is_word = True
            self.size += 1

    def contains(self, word) -> bool:
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if not cur.next.get(c):
                return False

            cur = cur.next.get(c)
        return cur.is_word

    def is_prefix(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            c = prefix[i]

            if not cur.next.get(c):
                return False
            cur = cur.next.get(c)

        return True


if __name__ == '__main__':
    print("Trie------------")

    trie = Trie()
    trie.add("hello")
    trie.add("happy")
    print(trie.contains("hello"))
    print(trie.contains("not"))

    print(trie.is_prefix('he'))







