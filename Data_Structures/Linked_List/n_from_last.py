class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def get_length(self):
        current = self.head
        count = 1
        while current.next is not None:
            count += 1
            current = current.next
        return count

    def insert_at_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

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

    # ------------------O(n) in 2 scan approach--------------------#
    def n_from_last(self, n):

        length = self.get_length()
        n = length - n
        if n < 0:
            return None

        i = 0
        current = self.head
        while i < n:
            current = current.next
            i = i + 1
        return current.data

    # ------------------O(n) in 1 scan approach--------------------#
    def n_from_last_efficient(self, n):
        if n < 0:
            return None
        current = self.head
        nth = self.head
        count = 1
        while count < n and current is not None:
            current = current.next
            count += 1

        if count < n or current is None:
            return None

        while current.next is not None:
            current = current.next
            nth = nth.next

        return nth.data


ll = LinkedList()
ll.insert_at_beg(8)
ll.insert_at_beg(7)
ll.insert_at_beg(6)
ll.insert_at_beg(5)
ll.print_ll()
print(ll.n_from_last_efficient(3))
print(ll.n_from_last(1))
