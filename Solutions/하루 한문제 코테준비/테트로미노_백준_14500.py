def dfs(sx,sy,count,score):
    global result
    if(result >= score+ maxVal*(3-count)):
        return

    if(count == 3):
        result = max(result, score)
        return

    else:
        for i in range(4):
            ex,ey = sx+dx[i],sy+dy[i]
            if(0<=ex<n and 0<=ey<m and (not visited[ex][ey])):
                if(count==1):
                    visited[ex][ey] = True
                    dfs(sx,sy,count+1,score+graph[ex][ey])
                    visited[ex][ey] = False

                visited[ex][ey] = True
                dfs(ex,ey,count+1,score+graph[ex][ey])
                visited[ex][ey] = False

n,m = map(int, input().split(" "))
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = -1


for i in range(n):
    graph.append(list(map(int,input().split(" "))))
maxVal = max(map(max,graph))
visited = [[False for q in range(m)] for w in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,0,graph[i][j])
        visited[i][j] = False
print(result)