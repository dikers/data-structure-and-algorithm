from graph_directed.Graph import Graph


class DirectedCycleDetection:

    def __init__(self, G: Graph):
        assert G.directed, "DirectedCycleDetection Only work in Directed Graph"
        self._order = []
        self.G = G
        self._has_cycle = False
        self.visited = [False] * G.get_v()
        self.on_path = [False] * G.get_v()
        for v in range(G.get_v()):
            if not self.visited[v]:
                if self.dfs(v):
                    self._has_cycle = True
                    break

    def dfs(self, v: int):
        # if self.visited[v]:
        #     return
        self.visited[v] = True
        self.on_path[v] = True

        for w in self.G.get_adj(v):
            if not self.visited[w]:
                if self.dfs(w):
                    return True
            elif self.on_path[w]:
                return True
        self.on_path[v] = False

        return False

    def has_cycle(self):
        return self._has_cycle




if __name__ == '__main__':

    graph = Graph('./data/ug.txt', True)
    print(graph)
    cd = DirectedCycleDetection(graph)
    print("has cycle: ", cd.has_cycle())


    graph = Graph('./data/ug2.txt', True)
    print(graph)
    cd = DirectedCycleDetection(graph)
    print("has cycle: ", cd.has_cycle())

