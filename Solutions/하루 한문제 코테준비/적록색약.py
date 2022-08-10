from collections import deque
def bfs(sx,sy,visited,red_green):
    q = deque()
    q.append([sx,sy])
    start = [graph[sx][sy]] if red_green==0 else (['R','G'] if graph[sx][sy]=='R'or graph[sx][sy]=='G' else [graph[sx][sy]])
    # print(start,sx,sy)
    while q:
        x,y = q.pop()
        visited[x][y] = True
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if(0<=nx<n and 0<=ny<n):
                if(not visited[nx][ny] and graph[nx][ny] in start):
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    # print(nx,ny)




dx,dy = [0,0,1,-1], [1,-1,0,0]
n = int(input())

graph = []
for i in range(n):
    graph.append(list(input()))

result = []
for i in range(2):
    visited = [[False for i in range(n)] for j in range(n)]
    temp_res = 0
    for j in range(n):
        for q in range(n):
            if(not visited[j][q]):
                temp_res += 1
                bfs(j,q,visited,i)
    # print('\n\n\n')
    result.append(temp_res)
print(*result)