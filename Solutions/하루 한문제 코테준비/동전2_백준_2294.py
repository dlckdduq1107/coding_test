n,k = map(int,input().split(" "))

coin = []
for i in range(n):
    coin.append(int(input()))

dp = [int(1e9) for i in range(k+1)]

dp[0] = 0
for c in coin:
    for j in range(c,k+1):
        dp[j] = min(dp[j],dp[j-c]+1)
    # print(dp)

if(dp[k]==int(1e9)):
    print(-1)
else:
    print(dp[k])
