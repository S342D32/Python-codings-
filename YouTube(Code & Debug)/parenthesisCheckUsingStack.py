def parenthesisChcekUsingStack(brackets):
  stack=[]

  for bracket in brackets:
    if bracket =="[" or bracket =="{" or bracket =="(":
       stack.append(bracket)
    else:
      if len(stack)==0:
        return False
      ch = stack.pop()
      if (bracket=="]" and ch =="[") or (bracket=="}" and ch =="{") or (bracket==")" and ch =="("):
        continue
      else:
        return False
  return len(stack) == 0

print(parenthesisChcekUsingStack("[[[[[(]]]]]"))

# TC = O(N)
# SC = O(N)


