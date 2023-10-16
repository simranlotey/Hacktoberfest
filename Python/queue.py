class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
# Create a new queue
q = Queue()

# Enqueue some items onto the queue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Dequeue an item from the queue
print(q.dequeue())  # Output: 1

# Get the front item in the queue
print(q.front())  # Output: 2

# Check if the queue is empty
print(q.is_empty())  # Output: False

# Get the size of the queue
print(q.size())  # Output: 2