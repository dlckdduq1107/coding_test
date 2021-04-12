import sys
# input = sys.stdin.readline
def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edge[j][0]
            next_node = edge[j][1]
            cost = edge[j][2]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur]+cost
                if i == n-1:
                    return True
    return False

INF = int(1e9)
n,m = map(int, input().split(" "))
edge = []
dist = [INF]*(n+1)

for i in range(m):
    a,b,c = map(int, input().split(" "))
    edge.append((a,b,c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])