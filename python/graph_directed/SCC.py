from graph_directed.Graph import Graph
from graph_directed.GraphDFS import GraphDFS

"""
联通分量， 分成几个独立的子图
"""
class SCC:
    def __init__(self, G: Graph):
        assert G.directed, " CC only works in undirected graph."

        self.G = G

        self.visited = [-1] * G.get_v()
        self.scccount = 0    #联通分量

        dfs = GraphDFS(G.reverse_graph(G))
        order = []
        for v in dfs.post():
            order.append(v)
        order.reverse()

        for v in order:
            if self.visited[v] == -1:
                self.dfs(v, self.scccount)
                self.scccount += 1

    def dfs(self, v: int, sccid: int):
        if self.visited[v] != -1:
            return
        self.visited[v] = sccid

        for w in self.G.get_adj(v):
            if self.visited[w] == -1:
                self.dfs(w, sccid)

    def get_cc(self):
        return self.scccount

    def get_visited(self):
        return self.visited

    # def validate_vertex(self, v: int):
    #     assert 0 <= v < self.G.get_v(), 'vertex {} is invalid'.format(v)

    def is_strongly_connected(self, v: int, w: int):
        self.G.validate_vertex(v)
        self.G.validate_vertex(w)
        return self.visited[v] == self.visited[w]

    def components(self):
        res = [[]]
        for i in range(self.scccount - 1):
            temp = []
            res.append(temp)
        for v in range(self.G.get_v()):
            res[self.visited[v]].append(v)
        return res


if __name__ == '__main__':

    graph = Graph('./data/ug2.txt', True)
    print(graph)
    degree = graph.indegree(3)
    print(degree)
    cc = SCC(graph)
    print("联通分量个数 ： ", cc.get_cc())
    print("联通分量 ： ", cc.get_visited())

    print(cc.is_strongly_connected(1, 2))
    print(cc.is_strongly_connected(1, 3))

    print("联通分量分组 ： ",cc.components())



