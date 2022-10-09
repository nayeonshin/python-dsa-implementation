class BinaryHeap(object):
    def __init__(self) -> None:
        self.items = [None]

    def __len__(self) -> int:
        return len(self.items) - 1

    # 삽입 시 실행, 반복 구조 구현
    def _percolate_up(self) -> None:
        i = len(self)
        parent_index = i // 2

        while parent_index > 0:
            if self.items[i] < self.items[parent_index]:
                self.items[parent_index], self.items[i] = self.items[i], self.items[parent_index]

            i = parent_index
            parent_index = i // 2

    def insert(self, k: int) -> None:
        self.items.append(k)
        self._percolate_up()

    # 추출 시 실행, 재귀 구조 구현
    def _percolate_down(self, i: int) -> None:
        left, right = i * 2, (i * 2) + 1
        smallest = i

        if (left <= len(self)) and (self.items[left] < self.items[smallest]):
            smallest = left

        if (right <= len(self)) and (self.items[right] < self.items[smallest]):
            smallest = right

        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self._percolate_down(smallest)

    def extract(self) -> int:
        root_value = self.items[1]

        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)

        return root_value
