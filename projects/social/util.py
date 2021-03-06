class Queue:
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)

    def empty(self):
        return self.size() == 0


class Stack:
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

    def empty(self):
        return self.size() == 0
