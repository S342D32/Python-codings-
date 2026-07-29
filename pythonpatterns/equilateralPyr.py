n =int(input("Enter a no.:"))
#where j is not for column ,it is for space

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for star in range(1,i+1):
#         print('*',end=" ")
#     print(' ')     

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for star in range(1,i+1):
#         print('*',end=" ")
#     print(' ')     



# o/t:
# Enter a no.:4
#    *  
#   * *
#  * * *
# * * * *
# _____________________________________________________
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for star in range(1,i+1):
#         print('*',end=" ")
#     print(' ')     
# for i in range(n-1,0,-1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for star in range(1,i+1):
#         print('*',end=" ")
#     print(' ')     
    
# o/t:
# Enter a no.:5
#     *  
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# ____________________________________________________________
# for i in range(n,0,-1):
#     for space in range(1,n-i+1):
#         print(end=" ")
#     for star in range(1,i+1):
#         print('*',end=" ")
#     print(' ')     
# for i in range(2,n+1):
#     for space in range(1,n-i+1):
#         print(end=" ")
#     for star in range(1,i+1):
#         print('*',end=" ")

#     print(' ')
# o/t:
# Enter a no.:5
# * * * * *  
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# for i in range(n,0,-1):
#    print(" "* (n-i),end=" ")
#    print("*"* (2*i-1))
# for i in range(2,n+1):
#     print(" "* (n-i),end=" ")
#     print("*"* (2*i-1))
# Enter a no.:5
#  *********
#   *******
#    *****
#     ***
#      *
#     ***
#    *****
#   *******
#  *********
# ________________________________________________________________-
# n = 5

# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         if i == n or k == 0 or k == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print('')
# *********
#  *     *
#   *   *
#    * *
#     *