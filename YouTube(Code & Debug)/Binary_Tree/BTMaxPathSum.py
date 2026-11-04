from collections import deque
from math import inf
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


def MaxSum(node):
  maxi =-inf
  def height(node):
    nonlocal maxi
    if node is None:
      return 0
    leftheight = height(node.left)
    if leftheight <0:
      leftheight= 0
    rightheight = height(node.right)
    if rightheight < 0:
        rightheight = 0
    maxi = max(maxi, leftheight + rightheight +node.val)
    return node.val +max(leftheight,rightheight)
  height(node)
  return maxi

print(MaxSum(one))

# TC=O(N)
# SC=O(H)

