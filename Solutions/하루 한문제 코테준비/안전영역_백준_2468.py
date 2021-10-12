from collections import deque
def bfs(sx,sy,limit,tempRes,visited):
    queue = deque([])

    if(visited[sx][sy]==False and graph[sx][sy]>limit):
        tempRes += 1
        visited[sx][sy] = True
        queue.append((sx,sy))

    while queue:
        v = queue.popleft()
        for i in range(4):
            nx,ny = v[0]+dx[i],v[1]+dy[i]
            if(0<=nx<n and 0<=ny<n):
                if(not visited[nx][ny] and graph[nx][ny]>limit):
                    queue.append((nx,ny))
                    visited[nx][ny] = True
    return tempRes

dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
graph = []
maxNum = -1
result = -1
for i in range(n):
    temp = list(map(int,input().split(" ")))
    maxNum = max(maxNum, max(temp))
    graph.append(temp)

for i in range(maxNum):
    tempRes = 0
    visited = [[False for q in range(n)] for w in range(n)]
    for r in range(n):
        for c in range(n):
            tempRes = bfs(r,c,i,tempRes,visited)
    result = max(result,tempRes)

print(result)