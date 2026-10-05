class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next =None


class QueueUsingDLL:
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self,item):
    new_node = Node(item)

    if self.head is None:
      self.head =self.tail= new_node
      return

    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node

  def dequeue(self):
    if self.head is None:
      return "Queue is empty"
    removed = self.head

    if self.head == self.tail:
      self.head= self.tail = None
      return removed.data
    
    self.head = self.head.next
    self.head.prev = None 
    return removed.data
  
  def rear(self):
    if self.head is None:
       return "Queue is empty"
    return self.tail.data
  def front(self):
    if self.head is None:
       return "Queue is empty"
    return self.head.data
  def print_all(self):
    curr = self.head
    while curr is not None:
      print(curr.data,end=" ")
      curr = curr.next




stack = QueueUsingDLL()

stack.enqueue(11)
stack.enqueue(12)
stack.enqueue(13)
# stack.dequeue()

print(stack.rear())
print(stack.front())

stack.print_all()

# TC=O(1) only print_all takesO(n) 
# SC=O(N)