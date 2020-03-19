from typing import List, Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self):
        self.storage: List[T] = []

    def push(self, value: T):
        self.storage.append(value)

    def pop(self):
        if not self.empty():
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)

    def empty(self):
        return self.size() == 0


class Stack(Generic[T]):
    def __init__(self):
        self.storage: List[T] = []

    def push(self, value: T):
        self.storage.append(value)

    def pop(self):
        if not self.empty():
            return self.storage.pop()
        else:
            return None

    def size(self):
        return len(self.storage)

    def empty(self):
        return self.size() == 0


def inverse_direction(direction: str):
    if direction == "n":
        return 's'
    elif direction == "s":
        return 'n'
    elif direction == "e":
        return 'w'
    elif direction == "w":
        return 'e'
    else:
        return None