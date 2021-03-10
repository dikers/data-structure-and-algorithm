from graph.Graph import Graph


class GraphDFS:

    def __init__(self, G: Graph):
        self._order = []
        self._pre = []
        self._post = []
        self.G = G
        self.visited = [False] * G.get_v()
        for i in range(G.get_v()):
            self.dfs(i)

    def dfs(self, v: int):
        if self.visited[v]:
            return
        self.visited[v] = True
        self._pre.append(v)

        for w in self.G.get_adj(v):
            if not self.visited[w]:
                self.dfs(w)
        self._post.append(v)

    def pre(self):
        return self._pre

    def post(self):
        return self._post

if __name__ == '__main__':

    graph = Graph('./data/data3.txt')
    print(graph)
    degree = graph.degree(5)
    print(degree)
    graphDFS = GraphDFS(graph)
    print("深度优先遍历  先序", graphDFS.pre())

    print("深度优先遍历  后向", graphDFS.post())
