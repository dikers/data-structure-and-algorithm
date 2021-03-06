"""
Leetcode 677

"""
class Node:
    def __init__(self,  val=0):

        self.next = dict()
        self.val = val


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for i in range(len(key)):
            c = key[i]
            if not cur.next.get(c):
                cur.next[c] = Node()
            cur = cur.next[c]

        cur.val = val;

    def sum(self, prefix: str) -> int:
        cur = self.root

        for i in range(len(prefix)):
            c = prefix[i]

            if not cur.next.get(c):
                return 0
            else:
                cur = cur.next.get(c)
        return self._sum(cur)

    def _sum(self, node: Node):

        if len(node.next) == 0:
            return node.val

        res = node.val
        for c in node.next.keys():
            res += self._sum(node.next.get(c))

        return res
