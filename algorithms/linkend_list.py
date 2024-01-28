class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkenList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.head = Node(value, self.head)
            self.length += 1
            return
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        temp.next = Node(value, temp.next)
        self.length += 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        prev = None
        next = None
        for _ in range(self.length):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    linked_list = LinkenList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.add(5)
    linked_list.print_list()
    linked_list.reverse()
    linked_list.print_list()
    linked_list.remove(2)
    linked_list.print_list()
    linked_list.insert(2, 3)
    linked_list.print_list()
    linked_list.set(2, 10)
    linked_list.print_list()
    print(linked_list.get(2))
    print(linked_list.length)
