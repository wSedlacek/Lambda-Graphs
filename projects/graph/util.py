
# Note: This Queue class is sub-optimal. Why?


class Queue():
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)


class Stack():
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.size() > 0:
            return self.storage.pop()
        else:
            return None

    def size(self):
        return len(self.storage)
