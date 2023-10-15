class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        return not (self.stack1 or self.stack2)

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def display(self):
        if not self.stack2:
            if not self.stack1:
                print("Queue is empty.")
                return
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        print("Front of the queue:", self.stack2[-1])
        print("Queue elements:", end=' ')
        for item in self.stack2:
            print(item, end=' ')
        print()

queue = QueueUsingTwoStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue elements after enqueue:", end=' ')
queue.display()

print("Dequeue operation:", queue.dequeue())

print("Queue elements after dequeue:", end=' ')
queue.display()

queue.enqueue(4)
queue.enqueue(5)

print("Queue elements after enqueue:", end=' ')
queue.display()

print("Peek operation:", queue.peek())

print("Is the queue empty?", queue.is_empty())

print("Queue size:", queue.size())
