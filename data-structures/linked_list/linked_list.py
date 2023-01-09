from typing import Optional

from node import Node


class LinkedList:  # Unordered linked list
    def __init__(self) -> None:
        self.head = None

    def print(self) -> None:
        """Print the values of all nodes in the list."""
        current = self.head

        while current:
            print(current.value)
            current = current.next

    def check_is_empty(self) -> bool:
        """Check if the list is empty."""
        return not self.head

    def get_size(self) -> int:
        """Get the size of the list."""
        size = 0
        current = self.head

        while current:
            size += 1
            current = current.next

        return size

    def search(self, value: int) -> bool:
        """Check if the list contains a node with the value."""
        current = self.head

        while current:
            if current.value == value:
                return True

            current = current.next

        return False

    def find(self, value: int) -> int:
        """Get the index of the first node with the value if it exists. Return -1 if not found."""
        index = 0
        current = self.head

        while current:
            if current.value == value:
                return index

            current = current.next
            index += 1

        return -1

    def add(self, node: Node) -> None:
        """Add the node at the head."""
        node.next = self.head
        self.head = node

    def _append(self, node: Node) -> None:
        """Append the node at the tail (end of the list)."""
        current = self.head

        if not current:
            self.head = node
        else:
            while current.next:
                current = current.next
            # Last node's next
            current.next = node

    def _insert(self, index: int, node: Node) -> None:
        """Insert a node at the index. Do nothing if the index is out of range (index < 0 or index > length)."""
        dummy_head = Node(0)
        dummy_head.next = self.head

        previous, current = dummy_head, dummy_head.next
        current_index = 0  # This essentially keeps track of the list's length.

        while current:
            if current_index == index:
                node.next = current
                previous.next = node
                # Moves previous to the new next
                previous = node

            current_index += 1
            previous, current = current, current.next

        # If `index` == (length of original linked list before inserting node), append node at tail.
        if current_index == index:
            previous.next = node

        # Updates self.head for the case of inserting node at the head
        self.head = dummy_head.next

    def pop(self, index: int) -> Optional[Node]:
        """Pop the node at the index. Return None if the index is out of range."""
        dummy_head = Node(0)
        dummy_head.next = self.head

        previous, current = dummy_head, dummy_head.next
        current_index = 0

        while current:
            if current_index == index:
                # Removes the current node
                previous.next = current.next
                # Updates self.head for the case of popping node at the head
                self.head = dummy_head.next
                return current

            current_index += 1
            previous, current = current, current.next

        return None

    def remove_first_match(self, value: int) -> None:
        """Remove the first node with the value if it exists."""
        dummy_head = Node(0)
        dummy_head.next = self.head

        previous, current = dummy_head, dummy_head.next

        while current:
            if current.value == value:
                previous.next = current.next
                self.head = dummy_head.next
                break

            previous, current = current, current.next

    def remove_all_matches(self, value: int) -> None:
        """Remove all the nodes with the value if any exists."""
        dummy_head = Node(0)
        dummy_head.next = self.head

        previous, current = dummy_head, dummy_head.next

        while current:
            if current.value == value:
                previous.next = current.next
                self.head = dummy_head.next
                current = current.next
            else:
                previous, current = current, current.next
