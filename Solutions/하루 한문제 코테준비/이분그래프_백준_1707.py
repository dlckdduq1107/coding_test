from collections import deque
# def dfs(start):
#     for i in graph[start]:
#         if(visited[i]):
#
#         else:
def bfs(start):
    visited[start] = 1
    q = deque([start])

    while q:
        current = q.popleft()
        for next in graph[current]:
            if(visited[next]==0):
                visited[next] = -visited[current]
                q.append(next)
            else:
                if(visited[next]==visited[current]):
                    return False
    return True

n = int(input())
for i in range(n):
    v,e = map(int,input().split())
    graph = [[] for j in range(v+1)]
    visited = [0 for q in range(v+1)]
    for j in range(e):
        start,end = map(int,input().split())
        graph[start].append(end)
        graph[end].append(start)
    flag = True
    for j in range(1,v+1):
        if(visited[j]==0):
            if not bfs(j):
                print('NO')
                flag = False
                break
    if(flag):
        print('YES')
