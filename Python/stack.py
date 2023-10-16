class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    # Create a new stack
s = Stack()

# Push some items onto the stack
s.push(1)
s.push(2)
s.push(3)

# Pop an item from the stack
print(s.pop())  # Output: 3

# Peek at the top item in the stack
print(s.peek())  # Output: 2

# Check if the stack is empty
print(s.is_empty())  # Output: False

# Get the size of the stack
print(s.size())  # Output: 2