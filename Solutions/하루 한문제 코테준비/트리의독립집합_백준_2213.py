def dfs(start):
    visited[start] = 1
    dp[start][0] = values[start]
    path[start][0].append(start)

    for i in graph[start]:
        if(not visited[i]):
            dfs(i)

            ##start포함할때
            dp[start][0] += dp[i][1] # start포함하면 그에 연결도니 i는 포함되면 안되므로 i포함X 를 더해준다.
            for j in path[i][1]:
                path[start][0].append(j)

            ##start포함X
            if(dp[i][0]<=dp[i][1]):
                dp[start][1] += dp[i][1]
                for j in path[i][1]:
                    path[start][1].append(j)
            else:
                dp[start][1] += dp[i][0]
                for j in path[i][0]:
                    path[start][1].append(j)



n = int(input())
values = [0]+list(map(int,input().split()))
graph = [[] for i in range(n+1)]
dp = [[0,0] for i in range(n+1)]
visited = [0 for i in range(n+1)]
path = [[[],[]] for i in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

if(dp[1][0]>dp[1][1]):
    result = 0
else:
    result =1

print(dp[1][result])
print(*sorted(path[1][result]))
