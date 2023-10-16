# Write a Python function to reverse a singly linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node3 = Node(3)
    node2.next = node3
    node4 = Node(4)
    node3.next = node4
    node5 = Node(5)
    node4.next = node5
    linked_list = LinkedList(node1)
    linked_list.print_list()
    linked_list.reverse()
    linked_list.print_list()


# Output:
# 1
# 2
# 3
# 4
# 5
# 5
# 4
# 3
# 2
# 1