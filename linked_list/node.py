from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self._value = value
        self._next = None

    @property
    def value(self) -> int:
        return self._value

    @property
    def next(self) -> Optional["Node"]:
        return self._next

    @value.setter
    def value(self, value: int) -> None:
        self._value = value

    @next.setter
    def next(self, next_: Optional["Node"]) -> None:
        self._next = next_
