n = int(input())
for j in range(n):
    q = int(input())
    dp = [0 for i in range(q)]
    if(q==1 or q==2):
        print(q)
        continue
    if(q==3):
        print(4)
        continue
    dp[0],dp[1],dp[2] = 1,2,4
    for i in range(3,q):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[q-1])