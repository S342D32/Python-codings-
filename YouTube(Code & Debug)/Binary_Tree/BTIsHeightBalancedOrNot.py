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
eight = Node(8)
nine=Node(9)

one.left =two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
seven.right = eight
eight.right = nine



def height(node):
    if node is None:
      return 0
    lh = height(node.left)
    if lh ==-1:
       return -1
    rh = height(node.right)
    if rh ==-1:
       return -1
    if abs(lh-rh) >1:
      return -1
    return 1 +max(lh,rh)

x = height(one)

if x == -1:
    print(False)
else:
    print(True)

# TC=O(N)
# SC=O(H)

