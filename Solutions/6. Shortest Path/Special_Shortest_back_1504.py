import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))# 자기자신은 0으로
    distance[start] = 0

    while q:# 우선순위 큐 사용
        dist,now = heapq.heappop(q)
        if distance[now] < dist:# 최단거리가 더 작으면 이미 확정이므로 패스
            continue
        for i in graph[now]: # 연결된 노드 탐색
            cost = dist + i[1]# 현재 노드의 최단거리 + 다음 노드까지의 거리
            if cost < distance[i[0]]:# 다음노드의 최단거리보다 구한cost가 더 작으면
                distance[i[0]] = cost# 다음 노드의 최단거리를 업데이트
                heapq.heappush(q,(cost,i[0]))# 힙에 다음노드에 대한 최단거리, 노드 넣어줌

INF = int(1e9)
v,e = map(int,input().split(" "))
graph = [[] for i in range(v+1)]


for i in range(e):
    a,b,c = map(int, input().split(" "))
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split(" "))

##순서바꾸기 위한 리스트 추가생성##
result1 = []
path1 = [1,v1,v2,v]
result2 = []
path2 = [1,v2,v1,v]

j = 0 # 1번째 반복
for i in path1[:3]:
    distance = [INF] * (v + 1)
    dijkstra(i)
    result1.append(distance[path1[j+1]])
    j += 1

j = 0# 2번째 반복
for i in path2[:3]:
    distance = [INF] * (v + 1)
    dijkstra(i)
    result2.append(distance[path2[j+1]])
    j += 1

if sum(result1) < sum(result2): # 둘중에 더 작은거 선택
    res = result1
else:
    res = result2

if INF in res:
    print(-1)
else:
    print(sum(res))