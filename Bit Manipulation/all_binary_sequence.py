def solve(index, flag, nums, result):
    if index >= len(nums):
        result.append("".join(nums))
        return

    # Always place 0
    nums[index] = "0"
    solve(index + 1, True, nums, result)

    # Place 1 only if previous character was not 1
    if flag == True:
        nums[index] = "1"
        solve(index + 1, False, nums, result)

    # Backtrack
    nums[index] = "0"


def generateBinaryStrings(n):
    nums = ["0"] * n
    result = []
    solve(0, True, nums, result)
    return result


print(generateBinaryStrings(3))

# TC=O(2^N)
# SC = O(N)