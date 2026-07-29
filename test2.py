n =5

for i in range(1,n+1):
  for space in range(1,n-i+1):
    print(" ",end="")
  for star in range(1,i+1):
    print("*",end=" ")
  print("")

   
for i in range(1,n-1):
  for space in range(1,n-2):
    print(" ",end="")
  for star in range(0,n-2):
    print("*",end=" ")
  print("")

for i in range(1,n-1):
  for space in range(1,n-2):
    print(" ",end="")
  for star in range(0,(n-2)*3):
    print("*",end=" ")

  for space in range((n-2)*3,n-2,-1):
    print(" ",end="")
  for star in range(0,(n-2)*3):
    print("*",end=" ")

  print("")
for i in range(1,n-1):
  for space in range(1,n-2):
    print(" ",end="")
  for star in range(0,n-2):
    print("*",end=" ")
  print("")



