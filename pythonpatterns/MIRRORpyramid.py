n = int(input("Enter no.:"))
# pyramid upside down on another pyramid
for i in range(n,0,-1):
    print(" "* (n-i),end=" ")
    print("*"*(2*i-1))

for i in range(2,n+i):
    print(" "* (n-i),end=" ")
    print("*"*(2*i-1))

# pyramid base over another pyramid
# for i in range(0,r):
#     print(" "* (r-i),end="")
#     print("*"*(2*i-1))

# for i in range(r,0,-1):
#     print(" "* (r-i),end="")
#     print("*"*(2*i-1))

