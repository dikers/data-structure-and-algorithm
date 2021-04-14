from graph_weighted.WeightedGraph import WeightedGraph

"""
联通分量， 分成几个独立的子图
"""
class CC:
    def __init__(self, G: WeightedGraph):
        # self._order = []
        self.G = G
        self.visited = [-1] * G.get_v()
        self.cccount = 0    #联通分量
        for v in range(G.get_v()):
            if self.visited[v] == -1:
                self.dfs(v, self.cccount)
                self.cccount += 1


    def dfs(self, v: int, cccount: int):
        if self.visited[v] != -1:
            return
        self.visited[v] = cccount

        for w in self.G.get_adj(v):
            if self.visited[w] == -1:
                self.dfs(w, cccount)

    def get_cc(self):
        return self.cccount

    def get_visited(self):
        return self.visited

    # def validate_vertex(self, v: int):
    #     assert 0 <= v < self.G.get_v(), 'vertex {} is invalid'.format(v)

    def is_connected(self, v: int, w: int):
        self.G.validate_vertex(v)
        self.G.validate_vertex(w)
        return self.visited[v] == self.visited[w]


    def components(self):

        res = [[]]
        for i in range(self.cccount - 1):
            temp = []
            res.append(temp)
        for v in range(self.G.get_v()):

            res[self.visited[v]].append(v)
        return res


if __name__ == '__main__':

    graph = WeightedGraph('./data/g.txt')
    print(graph)
    degree = graph.degree(5)
    print(degree)
    cc = CC(graph)
    print("联通分量 ： ", cc.get_cc())

    print("联通分量 ： ", cc.get_visited())

    print(cc.is_connected(1,2 ))
    print(cc.is_connected(1, 5))

    print(cc.components())



