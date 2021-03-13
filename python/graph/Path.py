"""

单源路径

"""


from graph.Graph import Graph


class Path:

    def __init__(self, G: Graph, s: int, t: int):
        self.G = G
        self._s = s
        self._t = t
        self.visited = [False] * G.get_v()
        self.pre = [-1] * self.G.get_v()

        self.G.validate_vertex(self._s)
        self.dfs(s, s)

    def dfs(self, v: int, parent: int) -> bool:

        if self.visited[v]:
            return
        self.pre[v] = parent
        self.visited[v] = True
        if v == self._t:
            return True
        for w in self.G.get_adj(v):
            if not self.visited[w]:
                if self.dfs(w, v):
                    return True
        return False

    def is_connected_to(self):
        return self.visited[self._t]

    def path(self):
        res = []
        if not self.is_connected_to():
            return res

        cur = self._t

        while cur != self._s:
            res.append(cur)
            cur = self.pre[cur]
        res.append(self._s)
        res.reverse()
        print("visited ", self.visited)
        return res
             

if __name__ == '__main__':

    graph = Graph('./data/data3.txt')
    print(graph)
    path = Path(graph, 0, 6)
    # graphDFS.dfs(1)
    # graphDFS.get_pre()
    print("is_connected_to", path.is_connected_to())
    print(path.path())


    path2 = Path(graph ,0, 1)
    print("0- -> 1: ", path2.path())

