def dfs(sx,sy):
    if(sx==m-1 and sy==n-1):
        return 1
    if(dp[sx][sy]!=-1):
        return dp[sx][sy]
    dp[sx][sy] = 0
    for i in range(4):
        nx,ny = sx+dx[i],sy+dy[i]
        if(0<=nx<m and 0<=ny<n):
            if(graph[sx][sy]>graph[nx][ny]):
                dp[sx][sy] += dfs(nx,ny)
    return dp[sx][sy]
dx,dy = [0,0,1,-1],[1,-1,0,0]
m,n = map(int,input().split(" "))
graph = []
for i in range(m):
    graph.append(list(map(int,input().split(" "))))

dp = [[-1 for i in range(n)] for j in range(m)]
# dp[0][0] = 1
# dfs(0,0)
print(dfs(0,0))
# for i in dp:
#     print(i)