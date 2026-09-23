from collections import deque

class Stack:
    def __init__(self):
        self.queue = deque()

    # Push element
    def push(self, item):
        self.queue.append(item)

        # Rotate the queue
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    # Pop top element
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue.popleft()

    # Top element
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue[0]

    # Check empty
    def is_empty(self):
        return len(self.queue) == 0

    # Size of stack
    def size(self):
        return len(self.queue)

# Testing
stack1 = Stack()

stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)

print("Stack size:", stack1.size())      # 4
print("Top element:", stack1.peek())     # 40
print("Pop:", stack1.pop())              # 40
print("Top after pop:", stack1.peek())   # 30
print("Stack size:", stack1.size())      # 3
print("Is Empty:", stack1.is_empty())    # False

# TC=O(1)
# SC=O(1)