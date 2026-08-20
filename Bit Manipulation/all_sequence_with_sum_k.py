nums = [2, 3, 5, 6, 8]

def backtrack(index, total, subset, target, result):

    if total == target:
        result.append(subset.copy())
        return

    elif total > target:
        return

    if index >= len(nums):
        return

    subset.append(nums[index])

    sum2 = total + nums[index]
    backtrack(index + 1, sum2, subset, target, result)

    e = subset.pop()
    sum2 = sum2 - e

    # Exclude current element
    backtrack(index + 1, total, subset, target, result)

target = 8
result = []

backtrack(0, 0, [], target, result)
print(result)

# TC = O(2^n)
# SC = O(n)