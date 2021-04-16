from graph_directed.Graph import Graph
from graph_directed.CC import CC
import copy

class DirectedEulerLoop:
    def __init__(self, G: Graph):
        self.G = G
        assert G.directed, "EulerLoop works in undirected graph"

        self._result = []

    def has_euler_loop(self) -> bool:
        # cc = CC(self.G)
        # print("联通分量 ： ", cc.get_cc())
        # if cc.get_cc() > 1:
        #     return False
        
        for v in range(self.G.get_v()):
            if self.G.indegree(v) != self.G.outdegree(v):
                return False
        return True

    def result(self):
        if not self.has_euler_loop():
            return self._result

        res = []
        stack = []
        g = copy.deepcopy(self.G)

        curv = 0

        stack.append(curv)
        while len(stack) > 0:
            if g.outdegree(curv) != 0:
                stack.append(curv)
                # print('**** ', list(g.adj[curv])[0])
                w = list(g.adj[curv])[0]
                g.remove_edge(curv, w)
                curv = w
            else:
                res.append(curv)
                curv = stack.pop()

        res.reverse()
        return res


if __name__ == '__main__':

    graph = Graph('./data/ug2.txt', True)
    print(graph)
    loop = DirectedEulerLoop(graph)
    print('有向图的欧拉回路', loop.result())


    graph = Graph('./data/ug3.txt', True)
    print(graph)
    loop = DirectedEulerLoop(graph)
    print('有向图的欧拉回路', loop.result())


