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
eight = Node(8)

one.left =two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
seven.right = eight

# Brute(level wise go)
# def RightSide(root):
#   if root is None:
#     return 0
#   result =[]
#   queue = deque()
#   queue.append(root )
#   while len(queue) != 0:
#     size = len(queue)
#     for i in range(len(queue)):
#       node = queue.popleft()
#       if i == size-1:   
#         result.append(node.val)
#       if node.left:
#         queue.append(node.left)
#       if node.right:
#         queue.append(node.right)
#   return result


# Optimal(reverse post order)

def RightSide(node,ans,level):
  if node is None:
    return 0
  if len(ans) == level:
    ans.append(node.val)
  if node.right:
    RightSide(node.right,ans,level+1)
  if node.left:
    RightSide(node.left, ans, level+1)
  return ans

ans=[]

print(RightSide(one,ans,0))

# TC=O(N)
# SC=O(H) stack space

