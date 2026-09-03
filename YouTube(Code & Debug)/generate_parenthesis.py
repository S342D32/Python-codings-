def solve(index,total,brackets,result):
  if index >=len(brackets):
    if total ==0:
      result.append("".join(brackets))
    return
  if total > len(brackets)//2:
    return
  if total <0:
    return
  brackets[index]="("
  sum = total+1
  solve(index+1,sum,brackets,result)
  brackets[index]=")"
  sum = total-1
  solve(index+1,sum,brackets,result)

n = 2
brackets = [""] * (2 * n)
result = []
solve(0, 0, brackets, result)
print(result)