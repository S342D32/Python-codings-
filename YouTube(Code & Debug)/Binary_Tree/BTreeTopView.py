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


def TopView(node):
  if node is None:
    return 0
  ans=[]
  result={}
  queue = deque()
  queue.append((node,0))
  while queue:
    e,line = queue.popleft()
    if line not in result:
      result[line]=e.val
    if e.left:
      queue.append((e.left,line-1))
    if e.right:
      queue.append((e.right,line+1))
  for value in sorted(result.items()):
    ans.append(value[1])
  return ans

TopView(one)
# TC=O(N + NlogN +N)
# SC=O(N+N)





print(TopView(one))

# TC=O(N)
# SC=O(H)

