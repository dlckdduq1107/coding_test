n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split(" "))))

dp = [[0 for i in range(n)] for j in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        move = graph[i][j]
        if(move!=0):
            if(i+move<n):
                dp[i+move][j] += dp[i][j]
            if(j+move<n):
                dp[i][j+move] += dp[i][j]

print(dp[-1][-1])
