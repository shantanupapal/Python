class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Doubly_LinkedList:
    def __init__(self, node=None):
        self.head = node

    def get_length(self):
        current = self.head
        count = 0
        while current.next is not None:
            count += 1
            current = current.next
        return count

    # ------------------INSERT--------------------#
    def insert_at_beg(self, data):
        newNode = Node(data, None, None)
        if self.head is None:
            self.head = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insert_at_end(self, data):
        newNode = Node(data, None, None)
        if self.head is None:
            self.insert_at_beg(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next

        newNode.next = None
        newNode.prev = current
        current.next = newNode

    def insert_at_pos(self, data, pos):
        if pos < 0 or pos > self.get_length() + 1:
            raise Exception('Invalid Index')

        if pos == 0:
            self.insert_at_beg(data)
            return

        current = self.head
        count = 0
        while current:
            if count == pos - 1:
                newNode = Node(data, None, None)
                newNode.next = current.next
                current.next = newNode
                newNode.prev = current
                break
            current = current.next
            count += 1

    # -------------------DELETE------------------#
    def del_at_beg(self):
        if self.head is None:
            print('Empty List')
        current = self.head
        self.head = current.next
        current.next.prev = None

    def del_at_end(self):
        if self.head is None:
            print('Empty List')
        current = self.head
        prev = self.head
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None

    def del_at_pos(self, pos):
        if pos < 0 or pos > self.get_length():
            raise Exception('Invalid Position')
        if pos == 0:
            self.del_at_beg()
        if pos == self.get_length():
            self.del_at_end()

        if self.head is None:
            print('Empty List')

        current = self.head
        previous = self.head
        count = 0
        while current:
            if count == pos:
                previous.next = current.next
                current.next.prev = previous

            previous = current
            current = current.next
            count += 1

    def del_value(self, value_to_del):
        if self.get_length() == 0:
            print('List is empty')

        current = self.head
        previous = self.head
        while current is not None:
            if current.data == value_to_del:
                break
            previous = current
            current = current.next

        if current is None:
            print('Value not found')
            return
        previous.next = current.next
        current.next.prev = previous

    def print_ll(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        ll = []
        current = self.head
        while current:
            ll.append(current.data)
            current = current.next
        print(ll)

    def clear(self):
        self.head = None


dll = Doubly_LinkedList()
dll.insert_at_beg(5)
dll.insert_at_beg(6)
dll.insert_at_beg(7)
dll.insert_at_end(4)
dll.insert_at_end(3)
dll.insert_at_pos(99, 0)
dll.print_ll()
dll.del_at_beg()
dll.print_ll()
dll.del_at_end()
dll.print_ll()
dll.del_at_pos(3)
dll.print_ll()
dll.del_value(6)
dll.print_ll()
