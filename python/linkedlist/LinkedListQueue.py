class Node:

    def __init__(self, e, next=None):
        self.e = e
        self.next = next

    def __str__(self):
        return str(self.e)


class LinkedListQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        if not self.tail:
            self.head = Node(e)
            self.tail = self.head
        else:
            self.tail.next = Node(e)
            self.tail = self.tail.next
        self.size += 1


    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue. "

        ret_node = self.head
        self.head = self.head.next
        ret_node.next = None

        if not self.head:
            self.tail = None
        self.size -= 1

    def get_front(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue. "

        return self.head.e

    def __str__(self):
        res = 'Queue: front  '
        cur = self.head

        first = True
        while cur:
            if first:
                first = False
            else:
                res += "->"
            res += str(cur.e)
            cur = cur.next

        res += '  tail'
        return res


if __name__ == '__main__':
    print("Linked List Stack Test.")

    queue = LinkedListQueue()

    for i in range(5):
        queue.enqueue(i)
        print(queue)

    queue.dequeue()
    queue.enqueue(10)
    queue.dequeue()

    print(queue)