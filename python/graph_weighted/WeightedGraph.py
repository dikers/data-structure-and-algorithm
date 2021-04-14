"""
邻接矩阵
"""


class WeightedGraph:

    def __init__(self, filename: str):

        self.V = 0    # 顶点
        self.E = 0    # 边数
        self.adj = []
        self.filename = filename
        with open(filename) as f:
            for i, line in enumerate(f.readlines()):

                if i == 0:
                    s1, s2 = line.split(",")
                    s1 = int(s1)
                    s2 = int(s2)
                    self.V = s1
                    assert self.V >= 0, 'V must be non-negative'
                    self.E = s2
                    assert self.E >= 0, 'E must be non-negative'
                    self.adj = [0] * s1

                    for j in range(self.V):
                        self.adj[j] = dict()
                    # print('init adj ', self.adj)
                else:
                    s1, s2, s3 = line.split(",")
                    s1 = int(s1)
                    s2 = int(s2)
                    weight = int(s3)
                    assert s1 != s2, 'Self loop is Detected! [{}][{}] '.format(s1, s2)
                    assert (s2,s3) not in self.adj[s1], 'Parallel Edges are Detected! [{}][{}] '.format(s1, s2)
                    self.validate_vertex(s1)
                    self.validate_vertex(s2)
                    # print('\ns1 [{}] s2 [{}] weight: [{}]'.format(s1, s2, s3) )

                    self.adj[s1][s2] = weight
                    self.adj[s2][s1] = weight
                    # print(self.adj)

            # print(self.adj)
    def validate_vertex(self, v: int):
        assert 0 <= v < self.V, 'vertex {} is invalid'.format(v)

    def remove_edge(self, v: int, w: int):
        self.validate_vertex(v)
        self.validate_vertex(w)
        if w in self.adj[v]:
            self.E -= 1
        self.adj[v].pop(w)
        self.adj[w].pop(v)

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
        return self.adj[v].keys()

    def get_weight(self, v: int, w: int):
        self.validate_vertex(v)
        self.validate_vertex(w)

        if self.has_edge(v, w):
            return self.adj[v][w]
        else:
            return -1


    def degree(self, v) -> int:
        self.validate_vertex(v)
        return len(self.get_adj(v))


if __name__ == '__main__':

    graph = WeightedGraph('./data/g.txt')
    print(graph)

    print('get_adj ', graph.get_adj(0))

    print(graph.degree(0))
    #
    #
    print("0 - 1   ", graph.get_weight(0, 1))
    print("0 - 2   ", graph.get_weight(0, 2))
    #
    #
    print("0 - 1   ", graph.has_edge(0, 1))
    print("0 - 2   ", graph.has_edge(0, 2))
    #
    # graph.remove_edge(0, 1)
    # print(graph)
   
