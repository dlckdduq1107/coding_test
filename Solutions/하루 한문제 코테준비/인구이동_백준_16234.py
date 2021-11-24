from collections import deque
def bfs(sx,sy):
    q = deque()
    q.append((sx,sy,0))
    visited[sx][sy] = True

    addList = [(sx,sy)]
    total = graph[sx][sy]
    while q:
        cx,cy,count = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if(0<=nx<n and 0<=ny<n):
                if(not visited[nx][ny] and (L<=abs(graph[cx][cy]-graph[nx][ny])<=R)):
                    q.append((nx,ny,count+1))
                    visited[nx][ny] = True
                    addList.append((nx,ny))
                    total += graph[nx][ny]
    for xx,yy in addList:
        graph[xx][yy] = total//len(addList)
    return len(addList)

dx,dy = [0,0,1,-1],[1,-1,0,0]
n,L,R = map(int,input().split(" "))
graph = []
for i in range(n):
    graph.append(list(map(int,input().split(" "))))

flag = True
count = 0
while flag:
    visited = [[False for w in range(n)] for q in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if(not visited[i][j]):
                open = bfs(i,j)
                if(open > 1):
                    flag = True
                    # for u in graph:
                    #     print(u)
                    # print()
    if flag:
        # print(count)
        count += 1



print(count)
