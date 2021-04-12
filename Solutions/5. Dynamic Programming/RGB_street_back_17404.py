n = int(input())
cost = [[0,0,0]]
for i in range(n):
    a,b,c = map(int, input().split(" "))
    cost.append([a,b,c])


INF = int(1e9)
res = []
for q in range(3): # 세가지 경우 탐색
    dp = [[0, 0, 0] for i in range(n + 1)] # 각각의 경우마다 dp생성
    for i in range(3):  # 1번째 값 초기화
        if q == i:
            dp[1][i] = cost[1][i]
        else:
            dp[1][i] = INF

    for i in range(2,n+1): # 다이내믹 실행
        dp[i][0] = cost[i][0]+min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for i in range(3): # 조건추가(n번째와 1번째가 같으면 안됨)
        if q != i:
            res.append(dp[n][i])
    # print(dp)
print(min(res))