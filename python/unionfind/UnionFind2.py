from unionfind.UF import UF


class UnionFind2(UF):

    def __init__(self, size: int):
        self.size = size

        self.parent = [0] * size

        for i in range(size):
            self.parent[i] = i

    def get_size(self) -> int:
        return len(self.id)

    def find(self, p: int) -> int:
        assert 0 <= p < len(self.parent), " p is out of bound. "

        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def is_connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def union_elements(self, p: int, q: int):

        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot == qRoot:
            return

        self.parent[pRoot] = qRoot

        
