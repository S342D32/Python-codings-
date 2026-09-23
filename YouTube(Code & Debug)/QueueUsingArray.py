class queue:
  def __init__(self):
    self.items=[]
  def is_empty(self):
    return len(self.items)==0
  def enqueue(self,item):
    self.items.append(item)
  def dequeue(self):
    if len(self.items)==0:
      return "Stack is empty"
    x = self.items.pop(0)
    return x
  def front(self):
    if len(self.items)==0:
      return "can not top, stack is empty"
    return self.items[0]
  def rear(self):
    if len(self.items)==0:
      return "can not top, stack is empty"
    return self.items[-1]
  def size(self):
    return len(self.items)

queue1 = queue()
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)
queue1.enqueue(6)
queue1.dequeue()

print(f"stack length={queue1.size()}")
print(f"front item={queue1.front()}")
print(f"rear item={queue1.rear()}")
print(f"stack length after pop={queue1.size()}")

# TC= O(N) because dequeue will adjust the elements to left after poping
# SC= O(N)

# If asked for the optimal Python implementation, use collections.deque with append() and popleft(), both O(1).