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


def Diameter(node):
  diameter =0

  def height(node):
    nonlocal diameter
    if node is None:
      return 0
    leftheight = height(node.left)
    rightheight = height(node.right)
    diameter = max(diameter, leftheight + rightheight)
    return 1 +max(leftheight,rightheight)
  height(node)
  return diameter

print(Diameter(one))

# TC=O(N)
# SC=O(H)

