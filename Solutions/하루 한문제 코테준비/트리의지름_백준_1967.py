import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(start,v):
    global result,next

    visited[start] = True
    for node,value in graph[start]:
        if(not visited[node]):
            if(result<v+value):
                result = v+value
                next = node

            dfs(node,v+value)

n = int(input())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

result = 0
next = 1
# for i in range(1,n+1):
visited = [False for j in range(n+1)]
dfs(next,0)

visited = [False for j in range(n+1)]
dfs(next,0)
print(result)