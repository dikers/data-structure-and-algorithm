from graph_weighted.CC import CC
import sys
from graph_weighted.WeightedGraph import WeightedGraph
from graph_weighted.WeightedEdge import WeightedEdge

class Prim:

    def __init__(self, G: WeightedGraph):
        self.G = G
        self.mst = []

        cc = CC(G)
        if cc.cccount > 1: # 不是连通图
            return

        self.edges = []
        visited = [False] * G.get_v()

        visited[0] = True


        for i in range(1, G.get_v()):
            minEdge = WeightedEdge(-1, -1, sys.maxsize )
            for v in range(G.get_v()):
                print("v  ", v)
                if visited[v]:
                    for w in G.get_adj(v):
                        if not visited[w] and G.get_weight(v, w) < minEdge.weight:
                            minEdge = WeightedEdge(v, w, G.get_weight(v, w))

            self.mst.append(minEdge)
            visited[minEdge.get_v()] = True
            visited[minEdge.get_w()] = True

    def result(self):
        # self.mst.sort()
        return self.mst

if __name__ == '__main__':

    graph = WeightedGraph('./data/g.txt')
    print(graph)

    prim = Prim(graph)
    for e in prim.result():
        print(e)