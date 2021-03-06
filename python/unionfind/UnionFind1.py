from unionfind.UF import UF


class UnionFind1(UF):
    def __init__(self, size: int):
        self.size = size
        self.id = [0] * size

        for i in range(size):
            self.id[i] = i

    def get_size(self) -> int:
        return len(self.id)

    def find(self, p: int) -> int:
        assert 0 <= p < len(self.id), " p is out of bound. "
        return self.id[p]

    def is_connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def union_elements(self, p: int, q: int):
        """
        合并元素p 和元素 q
        :param p:
        :param q:
        :return:
        """

        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return

        for i in range(len(self.id)):
            if pID == self.id[i]:
                id[i] = qID

