from linked_list import LinkedList
from node import Node


class OrderedLinkedList(LinkedList):
    def __init__(self) -> None:
        LinkedList.__init__(self)

    def search(self, value: int) -> bool:
        """Check if the list contains a node with the value."""
        current = self.head

        while current:
            if current.value == value:
                return True
            if current.value > value:
                return False

            current = current.next

        return False

    def find(self, value: int) -> int:
        """Get the index of the first node with the value if it exists. Return -1 if not found."""
        index = 0
        current = self.head

        while current:
            if current.value == value:
                return index
            if current.value > value:
                return -1

            current = current.next
            index += 1

        return -1

    def add(self, node: Node) -> None:
        """Add the node in the correct non-decreasing position."""
        dummy_head = Node(0)
        dummy_head.next = self.head

        previous, current = dummy_head, dummy_head.next

        while current and current.value < node.value:
            previous, current = current, current.next

        node.next = current
        previous.next = node

        self.head = dummy_head.next
