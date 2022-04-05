class Queue:
    def __init__(self):
        self.data = []
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self, value):
        self.data.append(value)
        self.length += 1

    def dequeue(self):
        first = self.data[0]
        self.data = self.data[1:]
        self.length -= 1
        return first

    def search(self, index):
        if self.length == 0 or index < 0 or index >= self.length:
            raise IndexError
        else:
            return self.data[index]
