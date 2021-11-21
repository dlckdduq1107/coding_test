from itertools import combinations
from collections import deque
import copy


def bfs(graph,init):
    global result
    q = deque()
    for sx,sy in init:
        q.append([sx,sy,0])
        graph[sx][sy] = 3
    temp = 0
    while q:
        cx,cy,count = q.popleft()

        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if(0<=nx<n and 0<=ny<n):
                if(graph[nx][ny] != 3):
                    if(graph[nx][ny]==1):
                        continue

                    if(graph[nx][ny]==0):
                        temp = count+1
                    graph[nx][ny] = 3
                    q.append((nx,ny,count+1))


    allSum = sum([sum(i) for i in graph])
    if(allSum == n*n*3-(wall*2)):
        result = min(result,temp)
        return True
    return False

result = int(1e9)
dx,dy = [0,0,1,-1],[1,-1,0,0]
n,m = map(int,input().split(" "))
graph = []
location = []
wall = 0
empty=0
for i in range(n):
    temp = list(map(int,input().split(" ")))
    for idx,j in enumerate(temp):
        if j == 2:
            location.append((i,idx))
        if j == 1:
            wall += 1
        if j==0:
            empty += 1
    graph.append(temp)

check = False
allResult = []
for virus in combinations(location,m):
    tempGraph = copy.deepcopy(graph)
    allResult.append(bfs(tempGraph,virus))
if(empty==0):
    print(0)
    exit(0)
if(True in allResult):
    print(result)
else:
    print(-1)