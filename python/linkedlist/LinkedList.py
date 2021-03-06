class Node:

    def __init__(self, e, next=None):
        self.e = e
        self.next = next

    def __str__(self):
        return str(self.e)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def add_first(self, e):
        self.head = Node(e, self.head)
        self.size += 1

    def add_last(self, e):
        self.add(self.size, e)

    def add(self, index: int,  e):
        assert index>=0 and index <self.size , "Add Failed. Illegal index"

        if index == 0:
            self.add_first(e)
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next

            # node = Node(e)
            # node.next = prev.next
            # prev.next = node

            prev.next = Node(e, prev.next)
            self.size += 1

                             
if __name__ == '__main__':
    print("Trie------------")

    ll = LinkedList()
    for i in range(10):
        ll.add_first(i)

    ll.add(1, 11)

    node = ll.head
    while node:
        print(node)
        node = node.next





