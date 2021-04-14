import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index =0

    def push(self, item, priority):
        # 传入两个参数，一个是存放元素的数组，另一个是要存储的元素，这里是一个元组。
        # 由于heap内部默认有小到大排，所以对priority取负数
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1



    def pop(self):
        return heapq.heappop(self._queue)[-1]


    def __len__(self):
        return len(self._queue)


q = PriorityQueue()

q.push('lenovo', 1)
q.push('Mac', 5)
q.push('ThinkPad', 2)
q.push('Surface', 3)

print(q)
print(q.pop())
# Mac
q.pop()
# Surface