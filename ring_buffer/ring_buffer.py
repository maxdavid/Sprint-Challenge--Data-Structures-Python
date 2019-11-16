from copy import copy


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current] = copy(item)
        if self.current >= self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        return [item for item in self.storage if item is not None]

