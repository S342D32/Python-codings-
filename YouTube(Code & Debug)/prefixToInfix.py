class Solution:
  def prefixToInfix(self,s):
    stack=[]
    for char in s[::-1]:
      # if char after is operand ,push it to the stack
      if char.isalNum():
        stack.append(char)
      else:
        # pop 2 operants but with reversed order
        operand1 = stack.pop()
        operand2 = stack.pop()

        # combine operands with operator
        new_expr = f"({operand2}{char}{operand1})"
        # push the result back onto the stack
        stack.append(new_expr)

    # Th final element in the stack is the infix expression
    return stack[-1]

