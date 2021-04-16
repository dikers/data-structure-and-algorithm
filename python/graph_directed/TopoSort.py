from graph_directed.Graph import Graph

class TopoSort:

    def __init__(self, G: Graph):
        assert G.directed, " TopoSort only works in directed graph"
        self.G = G
        self.res = []
        self._hasCycle = False
        self.in_degrees = [0] * G.get_v()

        q = []
        for v in range(G.get_v()):
            self.in_degrees[v] = G.indegree(v)
            if self.in_degrees[v] == 0:
                q.append(v)
        print("queue", q)

        while len(q) > 0:
            cur = q.pop()

            self.res.append(cur)

            for next in G.get_adj(cur):
                self.in_degrees[next] -= 1
                if self.in_degrees[next] ==0:
                    q.append(next)

        if len(self.res) != G.get_v():
            self._hasCycle = True
            self.res = []

    def hasCycle(self):
        return self._hasCycle

    def result(self):
        return self.res


if __name__ == '__main__':

    graph = Graph('./data/ug.txt', True)
    print(graph)
    topoSort = TopoSort(graph)
    print(topoSort.result())

    print("hasCycle ", topoSort.hasCycle())
    
