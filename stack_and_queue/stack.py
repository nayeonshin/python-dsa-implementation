class Stack:
    def __init__(self) -> None:
        self.stack = []

    def check_is_empty(self) -> bool:
        return not self.stack

    def get_size(self) -> int:
        return len(self.stack)

    def push(self, item: int) -> None:
        self.stack.append(item)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]
