from graph_weighted.CC import CC
import sys
from graph_weighted.WeightedGraph import WeightedGraph
from graph_weighted.WeightedEdge import WeightedEdge
from heap.PriorityQueue import PriorityQueue

"""
使用优先队列
"""
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

        pq = PriorityQueue()
        for w in G.get_adj(0):
            edge = WeightedEdge(0, w, G.get_weight(0, w))
            pq.push(edge, -1 * G.get_weight(0, w))

        while len(pq) > 0:
            minEdge = pq.pop()

            if visited[minEdge.v] and visited[minEdge.w]:
                continue

            self.mst.append(minEdge)
            newv = minEdge.w if visited[minEdge.v] else minEdge.v

            visited[newv] = True

            for w in G.get_adj(newv):
                if not visited[w]:
                    edge = WeightedEdge(newv, w, G.get_weight(newv, w))
                    pq.push(edge, -1 * G.get_weight(newv, w))

    def result(self):
        return self.mst

if __name__ == '__main__':

    graph = WeightedGraph('./data/g.txt')
    print(graph)

    prim = Prim(graph)
    for e in prim.result():
        print(e)