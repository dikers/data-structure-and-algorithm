
class WeightedEdge:

    def __init__(self, v: int, w: int, weight: int):

        self.v = v
        self.w = w
        self.weight = weight

    def get_v(self):
        return self.v

    def get_w(self):
        return self.w

    # def __cmp__(self, other):
    #     print("-------- cmp  ")
    #     return self.weight - other.weight
    #
    # def __ge__(self, other):
    #     return self.weight >= other.weight
    #
    # def __le__(self, other):
    #     return self.weight < other.weight

    def __gt__(self, other):
        # print("gt ")
        return self.weight >= other.weight
    def __lt__(self, other):
        return self.weight < other.weight
    

    def __str__(self):
        return '{}-{}: {}'.format(self.v, self.w, self.weight)