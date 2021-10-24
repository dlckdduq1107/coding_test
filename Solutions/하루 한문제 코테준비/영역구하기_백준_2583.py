import sys
sys.setrecursionlimit(10000)
def dfs(sx,sy,size):
    graph[sx][sy] = True
    for i in range(4):
        nx,ny = sx+dx[i],sy+dy[i]
        if(0<=nx<m and 0<=ny<n):
            if(not graph[nx][ny]):
                size = dfs(nx,ny,size+1)
    return size

dx,dy = [0,0,1,-1],[1,-1,0,0]
m,n,k = map(int,input().split(" "))
result = 0
sizes = []
graph = [[False for i in range(n)] for j in range(m)]
for i in range(k):
    sy,sx,ey,ex = map(int,input().split(" "))
    while(sx<ex):
        ty = sy
        while(ty<ey):
            graph[sx][ty] = True
            ty+=1
        sx+=1

for i in range(m):
    for j in range(n):
        if(not graph[i][j]):
            s = dfs(i,j,1)
            sizes.append(s)
            result+=1

print(result)
for i in sorted(sizes):
    print(i,end=" ")

