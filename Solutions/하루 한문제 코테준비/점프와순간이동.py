def solution(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    if n>1:
        dp[2] = 1
    if n < 3:
        return dp[n]

    for i in range(3,n+1):
        if(i%2==0):
            dp[i] = min(dp[i//2],dp[i-1]+1)
        else:
            dp[i] = dp[i-1]+1

    return dp[n]
print(solution(1))