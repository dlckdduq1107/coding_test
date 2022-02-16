import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def dfs(start):
    for i in tree[start]:
        if(visited[i]==0):
            visited[i] = start
            dfs(i)

n = int(input())

tree = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0 for i in range(n+1)]
dfs(1)

for i in range(2,n+1):
    print(visited[i])