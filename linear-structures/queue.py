class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.remove(self.items[0])

    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
