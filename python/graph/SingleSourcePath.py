"""

单源路径

"""


from graph.Graph import Graph


class SingleSourcePath:

    def __init__(self, G: Graph, s: int):
        self.G = G
        self._s = s
        self.visited = [False] * G.get_v()
        self.pre = [-1] * self.G.get_v()

        self.G.validate_vertex(self._s)
        self.dfs(s, s)

    def dfs(self, v: int, parent: int):

        if self.visited[v]:
            return
        self.pre[v] = parent
        self.visited[v] = True
        for w in self.G.get_adj(v):
            if not self.visited[w]:
                self.dfs(w, v)

    def get_pre(self):
        return self.pre

    def is_connected_to(self, target: int):
        self.G.validate_vertex(target)
        return self.visited[target]

    def path(self, t: int):
        res = []
        if not self.is_connected_to(t):
            return res

        cur = t

        while cur != self._s:
            res.append(cur)
            cur = self.pre[cur]
        res.append(self._s)
        res.reverse()
        
        return res
             



if __name__ == '__main__':

    graph = Graph('./data/data3.txt')
    print(graph)
    graphDFS = SingleSourcePath(graph, 0)
    # graphDFS.dfs(1)
    # graphDFS.get_pre()
    print(graphDFS.get_pre())
    print(graphDFS.path(6))


