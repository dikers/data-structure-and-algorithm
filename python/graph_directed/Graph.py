"""
有向无权图
"""
import copy


class Graph:

    def __init__(self, filename: str, directed=False):

        self.V = 0    # 顶点
        self.E = 0    # 边数
        self.adj = []
        self.filename = filename
        self.directed = directed

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
                    self.indegrees = [0] * self.V
                    self.outdegrees = [0] * self.V

                    for j in range(self.V):
                        self.adj[j] = set()
                    # print('init adj ', self.adj)
                else:
                    s1, s2 = line.split(",")
                    s1 = int(s1)
                    s2 = int(s2)
                    assert s1 != s2, 'Self loop is Detected! [{}][{}] '.format(s1, s2)
                    assert s2 not in self.adj[s1], 'Parallel Edges are Detected! [{}][{}] '.format(s1, s2)
                    self.validate_vertex(s1)
                    self.validate_vertex(s2)
                    # print('\ns1 [{}] s2 [{}] '.format(s1, s2) )
                    self.adj[s1].add(s2)

                    if self.directed:
                        self.outdegrees[s1] += 1
                        self.indegrees[s2] += 1

                    if not self.directed:
                        self.adj[s2].add(s1)

                    # print(self.adj)

        # print(self.adj)
    def validate_vertex(self, v: int):
        assert 0 <= v < self.V, 'vertex {} is invalid'.format(v)

    def reverse_graph(self, graph):
        rAdj = [0] * self.get_v()

        for v in range(self.get_v()):
            rAdj[v] = set()
            
        for v in range(self.get_v()):
            for w in self.adj[v]:
                rAdj[w].add(v)

        new_graph = copy.deepcopy(graph)
        self.adj = rAdj
        # self.directed = directed
        self.V = len(rAdj)    # 顶点
        self.E = 0          # 边数

        self.indegrees = [0] * self.V
        self.outdegrees = [0] * self.V

        for v in range(self.V):
            for w in self.adj[v]:
                self.outdegrees[v] += 1
                self.indegrees[w] += 1
                self.E += 1

        if not self.directed:
            self.E /= 2
        return new_graph
        


    def remove_edge(self, v: int, w: int):
        self.validate_vertex(v)
        self.validate_vertex(w)

        if w in self.adj[v]:
            self.E -= 1
            if self.directed:
                self.outdegrees[v] -= 1
                self.indegrees[w] -= 1

        self.adj[v].remove(w)
        if not self.directed:
            self.adj[w].remove(v)

    def __str__(self):

        print("邻接表-----{}-------Start".format(self.filename))
        print("节点数: {}     边数: {}   方向： {} ".format(self.V, self.E, self.directed))
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
        assert not self.directed, "Degree only works in undirected graph."

        self.validate_vertex(v)
        return len(self.get_adj(v))

    def indegree(self, v: int):
        assert self.directed, "InDegree only works in directed graph."
        self.validate_vertex(v)
        return self.indegrees[v]

    def outdegree(self, v: int):
        assert self.directed, "OutDegree only works in directed graph."
        self.validate_vertex(v)
        return self.outdegrees[v]







if __name__ == '__main__':

    graph = Graph('./data/ug.txt', True)
    print(graph)
    print("indegree 0 : ", graph.indegree(0))

    graph = Graph('./data/ug2.txt', True)
    print(graph)
    print("indegree 0: ", graph.outdegree(0))

    graph_reverse = graph.reverse_graph(graph)
    print(graph_reverse)
    print(graph)