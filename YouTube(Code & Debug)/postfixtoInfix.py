class Solution:
  def postToInfix(self,s):
    stack=[]
    for char in s:
      # if char is an operand, push it to the stack
      if char.isalnum():
        stack.append(char)
      else:
        operand2 = stack.pop()
        operand1 = stack.pop()

        new_expr = f"({operand1}{char}{operand2})"
        stack.append(new_expr)
    return stack[-1]

  # TC-O(N),SC-O(N)