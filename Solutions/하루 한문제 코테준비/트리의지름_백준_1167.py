import sys
input = sys.stdin.readline
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

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(1,len(temp)-2,2):
        graph[temp[0]].append([temp[j],temp[j+1]])

result = 0
next = 1
# for i in range(1,n+1):
visited = [False for j in range(n+1)]
dfs(next,0)

visited = [False for j in range(n+1)]
dfs(next,0)
print(result)