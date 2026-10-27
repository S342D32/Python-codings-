
# Brute force
# -----------------------------------------------
# def JumpMiniPlatformRequired(arr,index,jump):
#   last_index=len(arr)-1
#   if index >= last_index:
#     return jump
#   min_jump = float('inf')
#   for i in range(1,arr[index]+1):
#     min_jump = min(min_jump,JumpMiniPlatformRequired(arr,index+i,jump+1))
#   return min_jump

# arr = [2, 3, 1, 1, 4]
# print(JumpMiniPlatformRequired(arr,0,0))

# TC=O(N^N)
# SC=O(N)


def JumpMiniPlatformRequired(arr, index, dp):
    last_index = len(arr) - 1

    if index >= last_index:
        return 0

    if dp[index] != -1:
        return dp[index]

    min_jump = float('inf')

    for i in range(1, arr[index] + 1):
        if index + i < len(arr):
            result = JumpMiniPlatformRequired(arr, index + i, dp)

            if result != float('inf'):
                min_jump = min(min_jump, 1 + result)

    dp[index] = min_jump
    return dp[index]


arr = [2, 3, 1, 1, 4]
dp = [-1] * len(arr)

answer = JumpMiniPlatformRequired(arr, 0, dp)
print(-1 if answer == float('inf') else answer)


# Optimal solution