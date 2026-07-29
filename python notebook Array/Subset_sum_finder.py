def count_subset_sum(arr,target_sum):
    dp = [0] * (target_sum+1)
    dp[0]=1
    for num in arr:
        for i in range(target_sum,num-1,-1):
            dp[i] = (dp[i] + dp[i-num])
    return dp[target_sum]
def main():
    T = int(input("Enter no. of testcases:"))
    results =[]
    for _ in range(T):
        n = int(input("Enter size of array:"))
        arr = list(map(int,input("Enter array:").split()))
        target_sum = int(input("Enter target sum:"))
        results.append(count_subset_sum(arr,target_sum))
        for result in results:
            print(result)

if __name__ == "__main__":
    main()