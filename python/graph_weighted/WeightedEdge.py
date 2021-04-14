
class WeightedEdge:

    def __init__(self, v: int, w: int, weight: int):

        self.v = v
        self.w = w
        self.weight = weight

    def get_v(self):
        return self.v

    def get_w(self):
        return self.w

    def __str__(self):
        return '{}-{}: {}'.format(self.v, self.w, self.weight)