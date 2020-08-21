# Floyd Cycle Finding Algorithm
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def insert_at_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

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

    def create_cycle(self):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = self.head.next.next

    def isCyclic(self):
        fast = self.head
        slow = self.head

        while fast and slow:
            fast = fast.next
            print()
            if fast == slow:
                return True
            if fast is None:
                return False

            fast = fast.next
            if fast == slow:
                return True
            slow = slow.next


ll = LinkedList()
ll.insert_at_beg(8)
ll.insert_at_beg(7)
ll.insert_at_beg(6)
ll.insert_at_beg(5)
ll.insert_at_beg(9)
ll.insert_at_beg(10)
ll.insert_at_beg(11)
ll.insert_at_beg(15)
ll.insert_at_beg(18)
ll.insert_at_beg(17)
ll.insert_at_beg(16)
ll.insert_at_beg(19)
ll.create_cycle()
# ll.print_ll()
print(ll.isCyclic())
