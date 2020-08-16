class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def get_length(self):
        current = self.head
        count = 0
        while current.next is not None:
            count += 1
            current = current.next
        return count

    # --------------INSERT-------------------------#
    def insert_at_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beg(data)

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data, None)

    def insert_at_pos(self, data, pos):
        if pos < 0 or pos > self.get_length() + 1:
            raise Exception('Invalid Index')

        if pos == 0:
            self.insert_at_beg(data)
            return

        if pos == self.get_length() + 1:
            self.insert_at_end(data)
            return

        current = self.head
        count = 0
        while current:
            if count == pos - 1:
                newNode = Node(data, current.next)
                current.next = newNode
                break
            current = current.next
            count += 1

    # ----------------------DELETE----------------#
    def del_at_beg(self):
        if self.get_length() == 0:
            print('List is empty')
            return
        self.head = self.head.next

    def del_at_end(self):
        if self.get_length() == 0:
            print('List is empty')
        count = 0
        current = self.head
        while count < self.get_length() - 1:
            count += 1
            # print('current - ' + str(current.data))
            # print('next - ' + str(current.next.data))
            current = current.next
        current.next = None

    def del_at_pos(self, pos):
        if pos < 1 or pos > self.get_length() + 1:
            raise Exception('Invalid Index')

        if pos == 1:
            self.del_at_beg()
            return

        if pos == self.get_length() + 1:
            self.del_at_end()
            return

        pos = pos - 1
        current = self.head
        count = 0
        while count < pos - 1:
            # print('current - ' + str(current.data))
            # print('next - ' + str(current.next.data))
            current = current.next
            count += 1
        current.next = current.next.next

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
        current = None

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

ll = LinkedList()
ll.insert_at_beg(7)
ll.print_ll()
ll.insert_at_beg(6)
ll.print_ll()
ll.insert_at_beg(5)
ll.print_ll()
ll.insert_at_end(8)
ll.print_ll()
ll.insert_at_end(9)
ll.print_ll()
ll.insert_at_end(10)
ll.print_ll()
ll.insert_at_pos(11, 6)
ll.print_ll()
ll.del_at_beg()
ll.print_ll()
ll.del_at_end()
ll.print_ll()
ll.del_at_pos(3)
ll.print_ll()
ll.del_value(7)
ll.print_ll()
