n = int(input())
nums = list(map(int,input().split()))

dp = [0 for i in range(n+1)]
most_arr = [int(-1e9)]
max_len = int(-1e9)

for idx,each in enumerate(nums):
    if(most_arr[-1]<each):
        most_arr.append(each)
        dp[idx] = len(most_arr)-1
        max_len =  dp[idx]
    else:
        start,end = 0,len(most_arr)-1
        while(start<end):
            mid = (start+end)//2
            if(most_arr[mid]<each):
                start = mid + 1
            else:
                end = mid

        dp[idx] = start
        most_arr[start] = each

print(max_len)

