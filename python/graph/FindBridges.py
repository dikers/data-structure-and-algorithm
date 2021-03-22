from graph.Graph import Graph


class Edge:
    v = 0
    w = 0

    def __init__(self, v: int , w: int):
        self.v = v
        self.w = w

    def __str__(self):
        return "v: {}  w: {} ".format(self.v, self.w)

class FindBridges:

    def __init__(self, G: Graph):
        self._order = []
        self._low = []
        self._bridges = []
        self.G = G
        self.visited = [False] * G.get_v()
        self._order = [-1] * G.get_v()
        self._low = [-1] * G.get_v()
        self.cnt = 0
        for v in range(G.get_v()):
            if not self.visited[v]:
                self.dfs(v, v)


    def dfs(self, v: int, parent: int):
        if self.visited[v]:
            return
        self.visited[v] = True

        self._order[v] = self.cnt
        self.cnt += 1
        self._low[v] = self._order[v]


        for w in self.G.get_adj(v):
            if not self.visited[w]:
                self.dfs(w, v)
                self._low[v] = min(self._low[v], self._low[w])
                if self._low[w] > self._order[v]:
                    self._bridges.append(Edge(v, w))

            elif w != parent:
                self._low[v] = min(self._low[v], self._low[w])

    def bridges(self):
        return self._bridges

    def order(self):
        return self._order;
 


if __name__ == '__main__':

    graph = Graph('./data/bridge2.txt')
    print(graph)
    fd = FindBridges(graph)
    print(fd.order())
    bridges = fd.bridges()
    print(" 找到桥 ------------")
    for b in bridges:
        print(b)

    tree = Graph('./data/tree.txt')
    fd = FindBridges(tree)
    bridges = fd.bridges()
    print(" 找到桥 ------------")
    for b in bridges:
        print(b)

