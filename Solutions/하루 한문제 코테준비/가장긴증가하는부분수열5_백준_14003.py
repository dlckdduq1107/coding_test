from bisect import bisect_left
n = int(input())
nums = [0]+list(map(int,input().split()))

dp = [0 for i in range(n+1)]
most_arr = [int(-1e9)]
max_len = int(-1e9)

for i in range(1,n+1):
    if(most_arr[-1]<nums[i]):
        most_arr.append(nums[i])
        dp[i] = len(most_arr)-1
        max_len = dp[i]
    else:
        start,end = 0,len(most_arr)-1
        while(start<end):
            mid = (start+end)//2
            if(most_arr[mid]<nums[i]):
                start = mid + 1
            else:
                end = mid

        dp[i] = start
        most_arr[dp[i]] = nums[i]

print(max_len)

result = []
for i in range(n,0,-1):
    if(max_len==dp[i]):
        result.append(nums[i])
        max_len -= 1
print(*result[::-1])
# print(dp)
# print(most_arr)
