class Solution:
  def postToPre(self,s):
    stack=[]

    # post each character in postfix expression
    for char in s:
      # id character is an operant push it to the stack
      if char.isalnum():
        stack.append(char)
      else:
        # pop 2 operands from the stack
        operand1= stack.pop()
        operand2 = stack.pop()

        # combine the operands with operator in prefix form
        new_exp= f"{char}{operand1}{operand2}"

        # push the result back to the stack
        stack.append(new_exp)

    # The final element in the stack is the prefix expression
    return stack[-1]
  