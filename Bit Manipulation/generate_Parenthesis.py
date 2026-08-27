def solve(index,total,bracket,result):
  if index >= len(bracket):
    if total ==0:
      result.append("".join(bracket))
    return
  if total < 0:
    return
  elif total > len(bracket)//2:
    return
  bracket[index] ="("
  solve(index+1,total+1,bracket,result)
  bracket[index]=")"
  solve(index+1,total-1,bracket,result)

def generateParenthesis(n):
  result=[]
  bracket = [""] * (2*n)
  solve(0,0,bracket,result)
  return result
print(generateParenthesis(2))

# TC=O(2^N)
# SC = O(N)
