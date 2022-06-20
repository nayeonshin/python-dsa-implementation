from typing import Union

from binary_heap import BinaryHeap


class MinHeap(BinaryHeap):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, key: int) -> None:
        self.heap.append(key)
        self.size += 1
        self._percolate_up(self.size)

    def delete_min(self) -> Union[str, int]:
        # Checks if it is to 1 since the heap list was initialized with a value
        if len(self.heap) == 1:
            return "Empty heap"

        # Gets root of the heap (the min value of the heap)
        root = self.heap[1]
        # Moves the last value of the heap to the root
        self.heap[1] = self.heap[self.size]
        # Pops the last value since a copy was set on the root
        self.heap.pop()
        self.size -= 1
        # Moves down the root (value at index 1) to keep the heap property
        self._percolate_down(1)

        return root

    def _percolate_up(self, index: int) -> None:
        """Move the value up in the tree to maintain the heap property."""
        while index // 2 > 0:
            parent_index = index // 2

            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

            index = parent_index

    def _percolate_down(self, index: int) -> None:
        # If the current node has at least one child
        while (index * 2) <= self.size:
            # Gets the index of the min child of the current node
            min_child_index = self._get_min_child_index(index)

            # Swaps the values of the current element if it is greater than its min child
            if self.heap[index] > self.heap[min_child_index]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]

            index = min_child_index

    def _get_min_child_index(self, index: int) -> int:
        # If the current node has only one child, return the index of the unique child.
        left_child_index, right_child_index = index * 2, (index * 2) + 1
        if right_child_index > self.size:
            return left_child_index
        else:
            # Herein the current node has two children.
            # Returns the index of the min child according to their values
            if self.heap[left_child_index] < self.heap[right_child_index]:
                return left_child_index
            else:
                return right_child_index
