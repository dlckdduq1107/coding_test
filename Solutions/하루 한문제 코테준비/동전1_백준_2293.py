n,k = map(int,input().split(" "))
coin = []
for i in range(n):
    coin.append(int(input()))

dp = [0 for i in range(k+1)]

dp[0] = 1
for c in coin:
    for j in range(c,k+1):
        dp[j] += dp[j-c]

print(dp[k])