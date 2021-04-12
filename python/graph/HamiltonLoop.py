from graph.Graph import Graph


class HamiltonLoop:

    def __init__(self, G: Graph):
        self.G = G
        self.visited = [False] * G.get_v()
        self._pre = [-1] * G.get_v()
        self._end = -1

        self.dfs(0, 0, G.get_v())



    def dfs(self, v: int, parent: int, left: int)-> bool:

        if self.visited[v]:
            return
        self.visited[v] = True
        self._pre[v] = parent
        # print(v)
        left -= 1

        if left == 0 and self.G.has_edge(v, 0):
            self._end = v
            return True

        for w in self.G.get_adj(v):
            if not self.visited[w]:
                if self.dfs(w, v, left):
                    return True
            # elif w == 0 and self.all_visited():
            # elif w == 0 and left == 0:
            #
            #     self._end = v    # 最后一个节点的parent
            #     return True
        self.visited[v] = False         # 回溯
        left += 1
        return False

    def result(self):
        res = []
        if self._end == -1:
            return res


        cur = self._end

        while cur != 0:
            res.append(cur)
            cur = self._pre[cur]
        res.append(0)
        res.reverse()
        return res
                
    # def all_visited(self) -> bool:
    #
    #     for v in self.visited:
    #         if not v:
    #             return False
    #     return True



if __name__ == '__main__':

    graph = Graph('./data/hamilton1.txt')
    # print(graph)
    hamilton = HamiltonLoop(graph)
    print("end: ", hamilton._end)
    print(hamilton.result())


    graph = Graph('./data/hamilton2.txt')
    # print(graph)
    hamilton = HamiltonLoop(graph)
    print("end: ", hamilton._end)
    print(hamilton.result())

    
