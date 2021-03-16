"""
Unweighted Single Source Shortest Path
无权图单源最短路径
"""


from graph.Graph import Graph
from collections import deque


class USSSPath:

    def __init__(self, G: Graph, s: int):
        self.G = G
        self._s = s

        self._visited = [False] * G.get_v()
        self._pre = [-1] * G.get_v()
        self._dis = [-1] * G.get_v()

        self.bfs(self._s)

    def bfs(self, s: int):
        q = deque()
        q.append(s)
        self._visited[s] = True
        self._pre[s] = s
        self._dis[s] = 0

        while q:
            v = q.popleft()      # 队列左边出
            for w in self.G.get_adj(v):
                if not self._visited[w]:
                    q.append(w)
                    self._visited[w] = True
                    self._pre[w] = v
                    self._dis[w] = self._dis[v] + 1


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


    def dis(self, t: int):
        self.G.validate_vertex(t)
        return self._dis[t]



if __name__ == '__main__':

    graph = Graph('./data/g1.txt')
    print(graph)
    bfs = USSSPath(graph, 0)

    print("bfs pre: ", bfs.pre())

    print("path: ", bfs.path(6))

    print("dis : ", bfs.dis(6))