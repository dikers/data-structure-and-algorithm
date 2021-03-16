from graph.Graph import Graph


class CycleDetection:

    def __init__(self, G: Graph):
        self._order = []
        self.G = G
        self._has_cycle = False
        self.visited = [False] * G.get_v()
        for v in range(G.get_v()):
            if not self.visited[v]:
                if self.dfs(v, v):
                    self._has_cycle = True
                    break

    def dfs(self, v: int, parent: int):
        # if self.visited[v]:
        #     return
        self.visited[v] = True

        for w in self.G.get_adj(v):
            if not self.visited[w]:
                if self.dfs(w, v):
                    return True
            elif w != parent:
                return True

        return False

    def has_cycle(self):
        return self._has_cycle




if __name__ == '__main__':

    graph = Graph('./data/data3.txt')
    print(graph)
    degree = graph.degree(5)
    print(degree)
    cd = CycleDetection(graph)
    print("has cycle: ", cd.has_cycle())


    g2 = Graph('./data/g2.txt')
    cd2 = CycleDetection(g2)
    print("has cycle: ", cd2.has_cycle())
