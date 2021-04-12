INF = int(1e9)
v,e = map(int,input().split(" "))
graph = [[INF]*(v+1) for i in range(v+1)]
for i in range(e):
    a,b,c = map(int, input().split(" "))
    graph[a][b] = c

# for i in range(1,v+1): # 자기자신을 0으로 하면 안됨 자기자신으로 돌아오는 길도 고려할것이기 때문
#     for j in range(1,v+1):
#         if i == j:
#             graph[i][j] = 0

for k in range(1,v+1): # 플로이드 워셜알고리즘(자기자신으로 돌아오는 것도 포함<a->k->a>이렇게 다른곳을 거쳐서 돌아오는 경우도 고려
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b]) # a에서 b까지 직접가는 것 보다 k거쳐가는 것이 빠르면 업데이트

res = []
for i in range(1,v+1):
    for j in range(1,v+1):
        if i == j and graph[i][j] != INF: # 자기자신으로 돌아오는 것이 INF이면 사이클 없는거임
            res.append(graph[i][j]) # 있으면 추가

if res == []:
    print(-1)
else:
    print(min(res))