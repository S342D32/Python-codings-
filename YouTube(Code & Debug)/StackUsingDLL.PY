class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class StackUsingDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)

        # Stack is empty
        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.tail is None:
            return None

        popped = self.tail

        # Only one node
        if self.head == self.tail:
            self.head = self.tail = None
            return popped.data

        # Move tail backward
        self.tail = self.tail.prev
        self.tail.next = None

        return popped.data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"

        return self.tail.data

    def print_all(self):
        curr = self.head

        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


stack = StackUsingDLL()

stack.push(11)
stack.push(12)
stack.push(13)

print("Top:", stack.peek())
print("Pop:", stack.pop())
print("Top:", stack.peek())

stack.print_all()

# TC=O(1) only print_all takesO(n) 
# SC=O(N)