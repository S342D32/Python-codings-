class Queue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    # Enqueue (Push)
    def push(self, item):
        # Move all elements from st1 to st2
        while self.st1:
            self.st2.append(self.st1.pop())

        # Insert new element
        self.st1.append(item)

        # Move everything back to st1
        while self.st2:
            self.st1.append(self.st2.pop())

    # Dequeue (Pop)
    def pop(self):
        if self.is_empty():
            return "Queue is empty"
        return self.st1.pop()

    # Front element
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.st1[-1]

    # Check empty
    def is_empty(self):
        return len(self.st1) == 0

    # Queue size
    def size(self):
        return len(self.st1)


# Testing
q = Queue()

q.push(10)
q.push(20)
q.push(30)
q.push(40)

print("Queue size:", q.size())      # 4
print("Front:", q.peek())           # 10
print("Pop:", q.pop())              # 10
print("Front after pop:", q.peek()) # 20
print("Queue size:", q.size())      # 3

# TC=O(N)
# SC=O(N)