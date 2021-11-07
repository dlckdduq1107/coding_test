import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(sx,sy):
    if(visited[sx][sy]):
        return visited[sx][sy]

    visited[sx][sy] = 1
    currentValue = graph[sx][sy]
    for i in range(4):
        nx,ny = sx+dx[i],sy+dy[i]
        if(0<=nx<n and 0<=ny<n):
            nextValue = graph[nx][ny]
            if(currentValue<nextValue):
                visited[sx][sy] = max(visited[sx][sy],dfs(nx,ny)+1)

    return visited[sx][sy]


dx,dy = [0,0,1,-1],[1,-1,0,0]
n = int(input())
result = 0
graph = []
visited = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    graph.append(list(map(int,input().split(" "))))


for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j))

print(result)