n = int(input())

nums = [[0,0]]
for i in range(n):
    nums.append(list(map(int,input().split())))

dp = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(2,n+1):
    for j in range(1,n-i+2):
        dp[j][j+i-1] = min([ dp[j][j+q]+dp[j+q+1][i+j-1]+nums[j][0]*nums[j+q][1]*nums[i+j-1][1] for q in range(i-1)])

print(dp[1][n])