
def NextGreaterElement2(arr):
    n = len(arr)
    ans = [-1] * n
    stack = []

    for i in range(2*n - 1, -1, -1):
        while stack and stack[-1] <= arr[i%n]:
            stack.pop()

        if i<n:
            if stack:

               ans[i] = stack[-1]

        stack.append(arr[i%n])

    return ans


# TC: O(N)
# SC: O(N)

arr = [4, 5, 2, 10, 8]
print(NextGreaterElement2(arr))