from graph.Graph import Graph
from collections import deque


class SingleSourcePathBfs:

    def __init__(self, G: Graph, s: int):
        self.G = G
        self._s = s
        self._visited = [False] * G.get_v()
        self._pre = [-1] * G.get_v()

        self.bfs(self._s)

    def bfs(self, s: int):
        q = deque()
        q.append(s)
        self._visited[s] = True
        self._pre[s] = s

        while q:
            v = q.popleft()      # 队列左边出

            for w in self.G.get_adj(v):
                if not self._visited[w]:
                    q.append(w)
                    self._visited[w] = True
                    self._pre[w] = v

    def pre(self):
        return self._pre

    def is_connected_to(self, t: int):
        self.G.validate_vertex(t)
        return self._visited[t]

    def path(self, t: int):
        res = []
        if not self.is_connected_to(t):
            return res

        cur = t

        while cur != self._s:
            res.append(cur)
            cur = self._pre[cur]
        res.append(self._s)
        res.reverse()

        return res
        


if __name__ == '__main__':

    graph = Graph('./data/g1.txt')
    print(graph)
    bfs = SingleSourcePathBfs(graph, 0)

    print("bfs pre: ", bfs.pre())

    print("path: ", bfs.path(6))