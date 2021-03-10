from linkedlist.LinkedList import LinkedList


class LinkedListStack:

    def __init__(self):
        self.linkedList = LinkedList()

    def get_size(self):
        return self.linkedList.get_size()

    def is_empty(self):
        return self.linkedList.is_empty()

    def push(self, e):
        self.linkedList.add_first(e)

    def pop(self):
        self.linkedList.remove_first()

    def peek(self):
        self.linkedList.get_first()

    def __str__(self):
        res = "Stack: top "
        res += str(self.linkedList)
        return res


if __name__ == '__main__':
    print("Linked List Stack Test.")

    stack = LinkedListStack()

    for i in range(5):
        stack.push(i)
        print(stack)

    stack.pop()

    print(stack)