from graph_directed.Graph import Graph
from graph_directed.DirectedCycleDetection import DirectedCycleDetection
from graph_directed.GraphDFS import GraphDFS

class TopoSort2:

    def __init__(self, G: Graph):
        assert G.directed, " TopoSort only works in directed graph"
        self.G = G
        self.res = []
        directedCycleDetection = DirectedCycleDetection(G)
        self._hasCycle = directedCycleDetection.has_cycle()

        if self._hasCycle:
            print(" Topo Sort 2 只能用于无环图的拓扑排序")
            return

        dfs = GraphDFS(G)
        for v in dfs.post():
            self.res.append(v)
        self.res.reverse()
        

    def hasCycle(self):
        return self._hasCycle

    def result(self):                
        return self.res


if __name__ == '__main__':

    graph = Graph('./data/ug.txt', True)
    print(graph)
    topoSort = TopoSort2(graph)
    print(topoSort.result())

    print("hasCycle ", topoSort.hasCycle())

