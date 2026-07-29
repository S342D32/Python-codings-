n = 7

for i in range(1,n+1):
    
    for space in range(1,n-i+1):
        print(end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    for space in range(2*(n-i)):
        print(end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print(' ')

for i in range(n-1,0,-1):
    
    for space in range(1,n-i+1):
        print(end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    for space in range(2*(n-i)):
        print(end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print(' ')


#       *             *  
#      * *           * *
#     * * *         * * *
#    * * * *       * * * *
#   * * * * *     * * * * *
#  * * * * * *   * * * * * *
# * * * * * * * * * * * * * *
#  * * * * * *   * * * * * *
#   * * * * *     * * * * *
#    * * * *       * * * *
#     * * *         * * *
#      * *           * *
#       *             *