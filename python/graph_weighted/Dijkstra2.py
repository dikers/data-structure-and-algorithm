from graph_weighted.CC import CC
import sys
from graph_weighted.WeightedGraph import WeightedGraph
from graph_weighted.WeightedEdge import WeightedEdge
from heap.PriorityQueue import PriorityQueue


class Node:

    def __init__(self, v: int, dis: int):
        self.v = v
        self.dis = dis

    def __gt__(self, other):
        return self.dis >= other.dis


class Dijkstra:

    def __init__(self, G: WeightedGraph, s: int):
        self.G = G
        G.validate_vertex(s)
        self.s = s
        self.dis = [sys.maxsize] * G.get_v()
        self.dis[s] = 0
        self.pre = [-1] * G.get_v()
        self.visited = [False] * G.get_v()

        pq = PriorityQueue()
        pq.push(Node(s, 0), 0)
        self.pre[s] = s

        while len(pq) > 0:
            
            cur = pq.pop().v

            self.visited[cur] = True

            for w in G.get_adj(cur):
                if not self.visited[w]:
                    if self.dis[cur] + G.get_weight(cur, w) < self.dis[w]:

                        self.dis[w] = self.dis[cur] + G.get_weight(cur, w)
                        pq.push(Node(w, self.dis[w]), -1 * self.dis[w])
                        self.pre[w] = cur

    def result(self):
        return self.dis

    def is_connected_to(self, v: int) -> bool:
        self.G.validate_vertex(v)
        return self.visited[v]

    def is_dist_to(self, v:int) -> int:
        self.G.validate_vertex(v)
        return self.dis[v]


    def path(self, t:int):
        res = []

        if not self.is_connected_to(t):
            return res

        cur = t
        while cur != self.s:
            res.append(cur)
            cur = self.pre[cur]
        res.append(self.s)
        res.reverse()
        return res

if __name__ == '__main__':

    graph = WeightedGraph('./data/g2.txt')
    print(graph)

    dijkstra = Dijkstra(graph, 0)
    for e in dijkstra.result():
        print(e)

    print(dijkstra.is_connected_to(3))
    print(dijkstra.path(3))