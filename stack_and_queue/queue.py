class Queue:
    def __init__(self) -> None:
        self.queue = []

    def check_is_empty(self) -> bool:
        return not self.queue

    def get_size(self) -> int:
        return len(self.queue)

    def enqueue(self, item: int) -> None:
        self.queue.append(item)

    def dequeue(self) -> int:
        return self.queue.pop(0)
