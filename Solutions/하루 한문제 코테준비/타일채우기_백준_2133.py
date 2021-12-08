n = int(input())
dp = [0 for i in range(n+1)]
dp[0] = 1
if(n<2):
    print(0)
else:
    dp[2] = 3

    for i in range(4,n+1,2):
        dp[i] += dp[i-2]*3
        for j in range(i-4,-1,-2):
            dp[i] += dp[j]*2
    print(dp[n])

    