def dfs(sx,sy,count):

    global result
    result = max(result,count)
    for i in range(4):
        nx,ny = sx+dx[i],sy+dy[i]
        if(0<=nx<r and 0<=ny<c):
            current = graph[nx][ny]
            if(not visited[ord(current)-65]):
                # print(nx,ny)
                visited[ord(current)-65] = True
                dfs(nx,ny,count+1)
                visited[ord(current)-65] = False



dx,dy = [0,0,1,-1],[1,-1,0,0]
r,c = map(int,input().split(" "))
graph = []
result = -int(1e9)
visited = [False for i in range(26)]
for i in range(r):
    temp = list(input())
    graph.append(temp)

visited[ord(graph[0][0])-65] = True
dfs(0,0,1)
print(result)