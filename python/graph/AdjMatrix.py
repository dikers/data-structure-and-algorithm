"""
邻接矩阵
"""


class AdjMatrix:


    def __init__(self, filename: str):

        self.V = 0    # 顶点
        self.E = 0    # 边数
        self.adj = None
        self.filename = filename
        with open(filename) as f:
            for i, line in enumerate(f.readlines()):
                s1, s2 = line.split(",")
                s1 = int(s1)
                s2 = int(s2)
                if i == 0:
                    self.V = s1
                    assert self.V >= 0, 'V must be non-negative'
                    self.E = s2
                    assert self.E >= 0, 'E must be non-negative'
                    self.adj = [[0] * s1 for _ in range(s1)]
                else:
                    assert s1 != s2, 'Self loop is Detected! [{}][{}] '.format(s1, s2)
                    assert self.adj[s1][s2] != 1, 'Parallel Edges are Detected! [{}][{}] '.format(s1, s2)
                    self.validate_vertex(s1)
                    self.validate_vertex(s2)
                    self.adj[s1][s2] = 1
                    self.adj[s2][s1] = 1

            # print(self.adj)
    def validate_vertex(self, v: int):
        assert 0 <= v < self.V, 'vertex {} is invalid'.format(v)

    def __str__(self):

        print("邻接矩阵-----{}-------Start".format(self.filename))
        print("节点数: {}     边数: {} ".format(self.V, self.E))
        for row in self.adj:
            print(row)
        print("邻接矩阵---------------End")
        return ""

    def get_v(self) -> int:
        return self.V

    def get_e(self) -> int:
        return self.E

    def has_edge(self, v:int, w: int) -> bool:
        self.validate_vertex(v)
        self.validate_vertex(w)
        return self.adj[v][w] == 1

    def get_adj(self, v: int):

        res = []
        self.validate_vertex(v)
        for i in range(self.V):
            if self.adj[v][i] == 1:
                res.append(i)
        return res

    def degree(self, v) -> int:
        self.validate_vertex(v)
        return len(self.get_adj(v))



if __name__ == '__main__':

    adjMatrix = AdjMatrix('./data/g3.txt')
    # print(adjMatrix)
    degree = adjMatrix.degree(5)
    print(degree)
