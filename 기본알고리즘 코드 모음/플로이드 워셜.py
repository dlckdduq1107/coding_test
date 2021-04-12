INF = int(1e9)
v,e,end = map(int,input().split(" "))
graph = [[INF]*(v+1) for i in range(v+1)]
for i in range(e):
    a,b,c = map(int, input().split(" "))
    graph[a][b] = c

for i in range(1,v+1):
    for j in range(1,v+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b]) # a에서 b까지 직접가는 것 보다 k거쳐가는 것이 빠르면 업데이트

res = []
for i in range(1,v+1):
    res.append(graph[i][end]+graph[end][i])

print(max(res))


###노드가 500개 이상이면 플로이드 사용하면 안됨####
