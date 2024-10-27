class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


list1 = LinkedList()
list1.append(2)
list1.append(3)
list1.append(4)

print(list1.show_elements())


def reverse(l):
    if l.head is None:
        return

    current_node = l.head
    prev_node = None

    while current_node is not None:
        # Track the next node
        next_node = current_node.next

        # Modify the current node
        current_node.next = prev_node

        # Update prev and current
        prev_node = current_node
        current_node = next_node

    l.head = prev_node


reverse(list1)
print(list1.show_elements())
