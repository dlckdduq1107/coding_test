from collections import deque
import copy
def bfs(sx,sy,marker):
    q = deque()
    q.append([sx,sy])
    graph[sx][sy] = marker

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if(0<=nx<n and 0<=ny<n):
                if(graph[nx][ny]==1):
                    q.append([nx,ny])
                    graph[nx][ny] = marker
def bfsSearch(sx,sy,graph):
    global result
    if(graph[sx][sy]==0):
        return
    q = deque()
    q.append([sx,sy,0])

    marker = graph[sx][sy]
    while q:
        x,y,count = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if(0<=nx<n and 0<=ny<n and count<result):
                if(graph[nx][ny]==0):
                    q.append([nx,ny,count+1])
                    graph[nx][ny] = marker

                elif(graph[nx][ny]!=marker):
                    result = min(result,count)
    # for i in graph:
    #     print(i)
    # print(result)

result = int(1e9)
dx,dy = [0,0,1,-1],[1,-1,0,0]
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split(" "))))

marker = 2
for i in range(n):
    for j in range(n):
        if(graph[i][j]==1):
            bfs(i,j,marker)
            marker += 1

for i in range(n):
    for j in range(n):
        temp = copy.deepcopy(graph)
        bfsSearch(i,j,temp)

print(result)
# for i in graph:
#     print(i)