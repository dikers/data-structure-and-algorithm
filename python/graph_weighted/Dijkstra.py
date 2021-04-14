from graph_weighted.CC import CC
import sys
from graph_weighted.WeightedGraph import WeightedGraph
from graph_weighted.WeightedEdge import WeightedEdge
from heap.PriorityQueue import PriorityQueue


class Dijkstra:

    def __init__(self, G: WeightedGraph, s: int):
        self.G = G
        G.validate_vertex(s)
        self.s = s
        self.dis = [sys.maxsize] * G.get_v()
        self.dis[s] = 0
        self.visited = [False] * G.get_v()
        # visited[0] = True  # 不可设置为True
        while True:
            curdis = sys.maxsize
            cur = -1
            for v in range(G.get_v()):
                if not self.visited[v] and self.dis[v] < curdis:
                    curdis = self.dis[v]
                    cur = v

            if cur == -1:
                break

            self.visited[cur] = True

            for w in G.get_adj(cur):
                if not self.visited[w]:
                    if self.dis[cur] + G.get_weight(cur, w) < self.dis[w]:
                        self.dis[w] = self.dis[cur] + G.get_weight(cur, w)

    def result(self):
        return self.dis

    def is_connected_to(self, v: int) -> bool:
        self.G.validate_vertex(v)
        return self.visited[v]

    def is_dist_to(self, v:int)-> int:
        self.G.validate_vertex(v)
        return self.dis[v]

if __name__ == '__main__':

    graph = WeightedGraph('./data/g2.txt')
    print(graph)

    dijkstra = Dijkstra(graph, 0)
    for e in dijkstra.result():
        print(e)

    print(dijkstra.is_connected_to(2))