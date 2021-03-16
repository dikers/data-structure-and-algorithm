"""
邻接矩阵
"""


class Graph:

    def __init__(self, filename: str):

        self.V = 0    # 顶点
        self.E = 0    # 边数
        self.adj = []
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
                    self.adj = [0] * s1

                    for j in range(self.V):
                        self.adj[j] = set()
                    # print('init adj ', self.adj)
                else:
                    assert s1 != s2, 'Self loop is Detected! [{}][{}] '.format(s1, s2)
                    assert s2 not in self.adj[s1], 'Parallel Edges are Detected! [{}][{}] '.format(s1, s2)
                    self.validate_vertex(s1)
                    self.validate_vertex(s2)
                    # print('\ns1 [{}] s2 [{}] '.format(s1, s2) )
                    self.adj[s1].add(s2)
                    self.adj[s2].add(s1)
                    # print(self.adj)

            # print(self.adj)
    def validate_vertex(self, v: int):
        assert 0 <= v < self.V, 'vertex {} is invalid'.format(v)

    def __str__(self):

        print("邻接表-----{}-------Start".format(self.filename))
        print("节点数: {}     边数: {} ".format(self.V, self.E))
        for i, row in enumerate(self.adj):
            print("{} - {} ".format(i, row))
        print("邻接表---------------End")
        return ""

    def get_v(self) -> int:
        return self.V

    def get_e(self) -> int:
        return self.E

    def has_edge(self, v:int, w: int) -> bool:
        self.validate_vertex(v)
        self.validate_vertex(w)
        return w in self.adj[v]

    def get_adj(self, v: int):
        self.validate_vertex(v)
        return self.adj[v]

    def degree(self, v) -> int:
        self.validate_vertex(v)
        return len(self.get_adj(v))


if __name__ == '__main__':

    graph = Graph('./data/data.txt')
    print(graph)
    degree = graph.degree(5)
    print(degree)
