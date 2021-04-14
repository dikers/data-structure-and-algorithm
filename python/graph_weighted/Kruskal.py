from graph_weighted.CC import CC
from graph_weighted.WeightedGraph import WeightedGraph
from graph_weighted.WeightedEdge import WeightedEdge
from unionfind.UF import UF
from unionfind.UnionFind2 import UnionFind2
class Kruskal:

    def __init__(self, G: WeightedGraph):
        self.G = G
        self.mst = []

        cc = CC(G)
        if cc.cccount > 1:
            return

        self.edges = []
        for v in range(G.V):
            for w in G.get_adj(v):
                if v < w:
                    weightedEdge = WeightedEdge(v, w, G.get_weight(v, w))
                    self.edges.append(weightedEdge)
        self.edges.sort(key=lambda x:x.weight, reverse=False)
        # for e in self.edges:
        #     print(e)

        uf = UnionFind2(G.V)
        for edge in self.edges:
            # print(edge)
            v = edge.v
            w = edge.w
            # print(v, w)
            if not uf.is_connected(v, w):
                self.mst.append(edge)
                uf.union_elements(v, w)




    def result(self):
        return self.mst

if __name__ == '__main__':

    graph = WeightedGraph('./data/g.txt')
    print(graph)

    kruskal = Kruskal(graph)
    for e in kruskal.result():
        print(e)
    
