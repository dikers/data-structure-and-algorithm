"""
二分图检测
"""

"""
邻接矩阵
"""

from graph.Graph import Graph


class BipartitionDetection:

    def __init__(self, G: Graph):
        self.G = G
        self.visited = [False] * G.get_v()
        self._colors = [-1] * G.get_v()
        self._is_bipartite = True
        for v in range(G.get_v()):
            if not self.visited[v]:
                if not self.dfs(v, 0):
                    self._is_bipartite = False
                    break

    def dfs(self, v: int, color: int) -> bool:
        
        self.visited[v] = True
        self._colors[v] = color

        for w in self.G.get_adj(v):
            if not self.visited[w]:
                if not self.dfs(w, 1 - color):
                    return False

            elif self._colors[w] == self._colors[v]:
                return False

        return True

    def colors(self):
        if not self.is_bipartite():
            return None

        res = []
        colors1 = []
        colors2 = []
        for i, color in enumerate(self._colors):
            if color == 0:
                colors1.append(i)
            else:
                colors2.append(i)

        res.append(colors1)
        res.append(colors2)
        return res

    def is_bipartite(self):
        return self._is_bipartite


if __name__ == '__main__':

    graph = Graph('./data/g3.txt')  # 不是二分图
    print(graph)
    bd = BipartitionDetection(graph)
    print(bd.colors())
    print(bd.is_bipartite())


    graph2 = Graph('./data/g2.txt')  # 是二分图
    print(graph2)
    bd2 = BipartitionDetection(graph2)
    print(bd2.colors())
    print(bd2.is_bipartite())
