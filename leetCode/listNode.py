class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values):
        """Convert a Python list to a linked list."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    @staticmethod
    def print_linked_list(head):
        """Print all values from head to end."""
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next
