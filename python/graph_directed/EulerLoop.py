from graph_directed.Graph import Graph
from graph_directed.CC import CC
import copy

class EulerLoop:
    def __init__(self, G: Graph):
        self.G = G
        self._result = []

    def has_euler_loop(self) -> bool:
        cc = CC(self.G)
        print("联通分量 ： ", cc.get_cc())
        if cc.get_cc() > 1:
            return False
        for i in range(self.G.get_v()):
            if self.G.degree(i) % 2 == 1:
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
            if g.degree(curv) != 0:
                stack.append(curv)
                # print('**** ', list(g.adj[curv])[0])
                w = list(g.adj[curv])[0]
                g.remove_edge(curv, w)
                curv = w
            else:
                res.append(curv)
                curv = stack.pop()

        return res
        
 
if __name__ == '__main__':

    graph = Graph('./data/ug2.txt')
    # print(graph)
    loop = EulerLoop(graph)
    print(loop.result())


