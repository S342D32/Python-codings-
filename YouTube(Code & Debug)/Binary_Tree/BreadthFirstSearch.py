from collections import deque
class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

one =Node(1)
two =Node(2)
three =Node(3)
four =Node(4)
five =Node(5)
six = Node(6)
seven = Node(7)

one.left =two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven


def BreadthFirstSearch(node):
  result =[]
  queue = deque([])
  queue.append(node)
  while len(queue) != 0:
    current = queue.popleft()
    result.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return result

# TC=O(N)
# SC=O(N)

print(BreadthFirstSearch(one))
