from typing import Optional


class MinHeap:
    """Alternative implementation with different formulae for indices
    - parent index: (index - 1) // 2
    - left child index: (index * 2) + 1
    - right child index: (index * 2) + 2
    """
    def __init__(self) -> None:
        self.heap = []
        self.size = 0

    def insert(self, key: int) -> None:
        self.heap.append(key)
        self.size += 1
        self._percolate_up(self.size - 1)

    def delete_min(self) -> Optional[int]:
        if not self.heap:
            print("Empty heap")
            return None

        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]

        self.size -= 1
        minimum = self.heap.pop()
        self._percolate_down(0)

        return minimum

    def _percolate_up(self, index: int) -> None:
        while ((index - 1) // 2) >= 0:
            parent_index = (index - 1) // 2

            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

            index = parent_index

    def _percolate_down(self, index: int) -> None:
        while ((index * 2) + 1) < self.size:
            min_child_index = self._get_min_child_index(index)

            if self.heap[index] > self.heap[min_child_index]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]

            index = min_child_index

    def _get_min_child_index(self, index: int) -> int:
        left_child_index, right_child_index = (2 * index) + 1, (2 * index) + 2

        if right_child_index >= self.size:
            return left_child_index
        else:
            if self.heap[left_child_index] < self.heap[right_child_index]:
                return left_child_index
            else:
                return right_child_index
