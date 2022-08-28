class StackWithList:
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


class Node:
    def __init__(self, value: int, next_: "Node") -> None:
        self.value = value
        self.next = next_


class StackWithLinkedList:
    def __init__(self) -> None:
        self.top = None

    def push(self, value: int) -> None:
        self.top = Node(value, self.top)

    def pop(self) -> int:
        value = self.top.value
        self.top = self.top.next
        return value


stack = StackWithLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())
