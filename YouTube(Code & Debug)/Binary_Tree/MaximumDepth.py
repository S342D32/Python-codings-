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


def MaxDepth(node):
  if node is None:
    return 0
  leftHeight=MaxDepth(node.left)
  rightHeight=MaxDepth(node.right)
  return 1 + max(leftHeight,rightHeight)

# TC=O(N)
# SC=O(N)

print(MaxDepth(one))
