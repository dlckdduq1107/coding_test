from collections import deque
def bfs(sx,sy):
    global result
    q = deque()
    q.append([sx,sy,0])

    visited = [[False for i in range(row)] for j in range(col)]
    visited[sx][sy] = True
    while q:
        cx,cy,count = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if(0<=nx<col and 0<=ny<row):
                if(not visited[nx][ny] and graph[nx][ny]=='L'):
                    q.append([nx,ny,count+1])
                    visited[nx][ny] = True
                    result = max(result,count+1)



result = 0
dx,dy = [0,0,1,-1], [1,-1,0,0]
col,row = map(int, input().split(" "))
graph = []

for i in range(col):
    graph.append(list(input()))

for i in range(col):
    for j in range(row):
        if(graph[i][j]=='L'):
            bfs(i,j)

print(result)
