"""
邻接矩阵
"""


class AdjMatrix:

    def __init__(self, filename: str):

        self.V = 0    # 顶点
        self.E = 0    # 边数
        self.adj = None
        self.filename = filename
        with open(filename) as f:
            for i, line in enumerate(f.readlines()):
                s1, s2 = line.split(",")
                s1 = int(s1)
                s2 = int(s2)
                if i == 0:

                    self.V = s1
                    self.E = s2
                    self.adj = [[0] * s1 for _ in range(s1)]
                    # print(self.adj)
                else:
                    self.adj[s1][s2] = 1
                    self.adj[s2][s1] = 1

            # print(self.adj)

    def __str__(self):

        print("邻接矩阵-----{}-------Start".format(self.filename))
        print("节点数: {}     边数: {} ".format(self.V, self.E))
        for row in self.adj:
            print(row)
        print("邻接矩阵---------------End")
        return ""


if __name__ == '__main__':


    adjMatrix = AdjMatrix('data.txt')
    print(adjMatrix)
