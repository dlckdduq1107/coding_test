import copy
import sys
sys.setrecursionlimit(10000)
def dfs(sx,sy,count,graph,visited):
    global result
    result = max(result,count)
    visited[sx][sy] = True
    currentValue = graph[sx][sy]
    # if currentValue:
    #
    # else:
    for i in range(4):
        nx,ny = sx+dx[i],sy+dy[i]
        if(0<=nx<n and 0<=ny<n):
            nextValue = graph[nx][ny]
            if(currentValue<nextValue and not visited[nx][ny]):
                visited[nx][ny] = True
                dfs(nx,ny,count+1,graph,visited)
                # print(count,sx,sy,nx,ny)
                visited[nx][ny] = False

    # return count


dx,dy = [0,0,1,-1],[1,-1,0,0]
n = int(input())
result = 0
graph = []
for i in range(n):
    graph.append(list(map(int,input().split(" "))))

for i in range(n):
    for j in range(n):
        cpyGraph = copy.deepcopy(graph)
        visited = [[False for i in range(n)] for j in range(n)]
        dfs(i,j,1,cpyGraph,visited)

print(result)