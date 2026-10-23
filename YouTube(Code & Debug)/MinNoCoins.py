# def MinNoCoins(arr,k):
#   result =[]
#   n = len(arr)
#   for i in range(n-1,-1,-1):
#     while k >= arr[i]:
#       result.append(arr[i])
#       k -= arr[i]
#   return result

# arr = [2,4,3,1,7,9,8,7]
# print(MinNoCoins(arr,11))
# TC=O(N)
# SC=O(1)

# -----------------------------------------
# For Greedy approch we have to sort
def MinNoCoins(arr, k):
    arr.sort(reverse=True)
    result = []

    for coin in arr:
        while k >= coin:
            result.append(coin)
            k -= coin

    if k != 0:
        return -1

    return result

# TC=O(NlogN + k)
# Space complexity (SC)
# - Sorting in place: typically \(O(N)\) auxiliary space in Python's implementation.
# - result list: up to \(O(K)\) space for positive integer denominations.
# SC=O(N+k)
arr = [2, 4, 3, 1, 7, 9, 8, 7]
print(MinNoCoins(arr, 11))