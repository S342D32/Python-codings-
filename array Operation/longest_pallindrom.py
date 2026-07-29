def longest_pallindrom(s):
  def find_pallin(left,right):
    while left >=0 and right < len(s) and s[left] == s[right]:
      left-=1
      right+=1
    return s[left+1:right]
  longest =""
  for i in range(len(s)):
    odd_pallin = find_pallin(i,i)
    if len(odd_pallin) > len(longest):
      longest = odd_pallin
    even_pallin = find_pallin(i,i+1)
    if len(even_pallin) > len(longest):
      longest = even_pallin
  return longest

s = "strabaabbadt"
print(longest_pallindrom(s))
