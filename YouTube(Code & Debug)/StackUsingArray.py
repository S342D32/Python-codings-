class stack:
  def __init__(self):
    self.items=[]
  def is_empty(self):
    return len(self.items)==0
  def push(self,item):
    self.items.append(item)
  def pop(self):
    if len(self.items)==0:
      return "Stack is empty"
    x = self.items.pop()
    return x
  def top(self):
    if len(self.items)==0:
      return "can not top, stack is empty"
    return self.items[-1]
  def size(self):
    return len(self.items)

stack1 = stack()
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
print(f"stack length={stack1.size()}")
print(f"poped item={stack1.pop()}")
print(f"top item={stack1.top()}")
print(f"stack length after pop={stack1.size()}")

# TC= O(1)
# SC= O(N)