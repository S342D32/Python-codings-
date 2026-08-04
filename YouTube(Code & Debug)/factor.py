def factors(n):
  f=[]
  for i in range(1,n+1):
    if n%i ==0:
      f.append(i)
  return f

print(factors(10))