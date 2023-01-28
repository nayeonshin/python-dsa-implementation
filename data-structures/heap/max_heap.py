from typing import Union

from binary_heap import BinaryHeap


class MaxHeap(BinaryHeap):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, key: int) -> None:
        self.heap.append(key)
        self.size += 1
        self._percolate_up(self.size)

    def delete_max(self) -> Union[str, int]:
        if len(self.heap) == 1:
            return "Empty heap"

        maximum = self.heap[1]

        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self._percolate_down(1)

        return maximum

    def _percolate_up(self, index: int) -> None:
        while (index // 2) > 0:
            parent_index = index // 2

            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

            index = parent_index

    def _percolate_down(self, index: int) -> None:
        while (index * 2) <= self.size:
            max_child_index = self._get_max_child_index(index)

            if self.heap[index] < self.heap[max_child_index]:
                self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]

            index = max_child_index

    def _get_max_child_index(self, index: int) -> int:
        left_child_index, right_child_index = index * 2, (index * 2) + 1

        if right_child_index > self.size:
            return left_child_index
        else:
            if self.heap[left_child_index] < self.heap[right_child_index]:
                return left_child_index
            else:
                return right_child_index
