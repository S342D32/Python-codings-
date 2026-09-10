def solve(index,subset,digits,result,char_map):
  if index >= len(digits):
    result.append("".join(subset))
    return
  for char in char_map[digits[index]]:
    subset.append(char)
    solve(index+1,subset,digits,result,char_map)
    subset.pop()
  return result
char_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
print(solve(0,[],"49978898893",[],char_map))

# TC=