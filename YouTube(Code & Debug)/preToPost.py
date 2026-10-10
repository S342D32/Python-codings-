class Solution:
  def preToPost(self,s):
    stack =[]
# traverse the prefix expressions from right to left using index
    n = len(s)
    for i in range(n-1,-1,-1):
      char =s[i]

      # if the character is an operand push it to the stack
      if char.isalnum():
        stack.append(char)
      else:

        opr1= stack.pop()
        opr2= stack.pop()

        new_exp= opr1+ opr2+char

        stack.append(new_exp)
    return stack[-1]

  