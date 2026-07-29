n = int(input("Enter a no:"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print('')
# o/t:
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for star in range(1,i+1):
#         print('*',end=" ")
#     print(' ')     


# ___________________________________________________________________
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print('')
#     # ONLY CHANGE IN THE (N-1,0,-1) TOO start from last 
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print('')
# O/T: 
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# _____________________________________________
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print('')
# for i in range(2,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print('')
# o/t:
# Enter a no:6
# 6 6 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# _____________________________________________
# current_num =1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(current_num,end=" ")
#         current_num +=1

#     print('')
    
# o/t:
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# __________________________________________________

# n = int(input("Enter no:"))


# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end ="")
#     for space in range(1,2*(n-i)+1):
#         print(" ",end="")
#     for j in range(i,0,-1):
#         print(j,end ="")
#     print('')
    
        

# O/T:
# Enter no:6
# 123456654321
# 12345  54321
# 1234    4321
# 123      321
# 12        21
# 1          1

def staircase(n):
    for i in range(1, n + 1):
        # Calculate spaces and hashes
        spaces = ' ' * (n - i)
        hashes = '#' * i
        # Print the staircase line
        print(spaces + hashes)

# Input size of the staircase
n = int(input("Enter the size of the staircase: "))
staircase(n)
____________
     #
    ##
   ###
  ####
 #####
######
___________________
n = int(input("Enter a no:"))

for i in range(1, n+1):
    # Print the first half of the pattern
    for j in range(1, i+1):
        print(j, end=" ")
    
    # Calculate spaces
    spaces = (n - i) * 4
    print(" " * spaces, end="")
    
    # Print the mirrored pattern
    for j in range(i,0,-1):
        print(j, end=" ")
    
    # Move to the next line after each row
    print('')
_____________

# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1