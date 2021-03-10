class Node:

    def __init__(self, e, next=None):
        self.e = e
        self.next = next

    def __str__(self):
        return str(self.e)


class LinkedList:

    def __init__(self):

        self.dummy_head = Node(None, None)
        self.size = 0

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def add_first(self, e):
        self.add(0, e)

    def add_last(self, e):
        self.add(self.size, e)

    def add(self, index: int,  e):
        assert 0 <= index <= self.size  , "Add Failed. Illegal index"

        prev = self.dummy_head
        for _ in range(index):
            prev = prev.next

        # node = Node(e)
        # node.next = prev.next
        # prev.next = node

        prev.next = Node(e, prev.next)
        self.size += 1

    def get(self, index: int):
        prev = self.dummy_head.next
        for _ in range(index):
            prev = prev.next

        return prev.e

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self.size - 1)

    def set(self, index: int , e):
        assert 0 <= index <= self.size  , "Add Failed. Illegal index"

        prev = self.dummy_head.next
        for _ in range(index):
            prev = prev.next
        prev.e = e

    def contains(self, e) -> bool:
        cur = self.dummy_head.next

        while cur:
            if cur.e == e:
                return True
            cur = cur.next
        return False

    def delete(self, index: int):
        assert 0 <= index < self.size, "Add Failed. Illegal index"

        prev = self.dummy_head
        for _ in range(index):
            prev = prev.next

        del_node = prev.next
        prev.next = del_node.next
        del_node.next = None
        self.size -= 1
        return del_node

    def remove_first(self):
        return self.delete(0)

    def remove_last(self):
        return self.delete(self.size-1)

    def __str__(self):
        res = '[dummy'
        cur = self.dummy_head.next

        while cur:
            res += " -> "
            res += str(cur.e)
            cur = cur.next

        res += ' ->NULL ]'
        return res


                             
if __name__ == '__main__':
    print("Trie------------")

    ll = LinkedList()
    for i in range(10):
        ll.add_first(i)

    ll.add(1, 11)

    node = ll.dummy_head
    while node:
        print(node)
        node = node.next


    print("get({}) {} ".format(4 , ll.get(4)))

    ll.set(4, 99)
    print("get({}) {} ".format(4 , ll.get(4)))

    print(" get first ", ll.get_first())
    print(" get last  ", ll.get_last())


    print('contains: ', ll.contains(99))

    print(ll)
    ll.remove_first()
    ll.remove_last()
    print(ll)








