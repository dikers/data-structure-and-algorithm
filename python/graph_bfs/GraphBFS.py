from graph.Graph import Graph
from collections import deque
 

class GraphBFS:

    def __init__(self, G: Graph):
        self.G = G
        self._visited = [False] * G.get_v()
        self._order = []

        for v in range(G.get_v()):
            if not self._visited[v]:
                self.bfs(v)

    def bfs(self, s: int):
        q = deque()
        q.append(s)
        self._visited[s] = True

        while q:
            v = q.popleft()      # 队列左边出
            self._order.append(v)

            for w in self.G.get_adj(v):
                if not self._visited[w]:
                    q.append(w)
                    self._visited[w] = True

    def order(self):
        return self._order

    def pre(self):
        return self._pre



                
if __name__ == '__main__':

    graph = Graph('./data/g3.txt')
    print(graph)
    bfs = GraphBFS(graph)
    print("bfs  order: ", bfs.order())
