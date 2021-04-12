import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))# 자기자신은 0으로
    distance[start] = 0

    while q:# 우선순위 큐 사용
        dist, now = heapq.heappop(q)
        if distance[now] < dist:# 최단거리가 더 작으면 이미 확정이므로 패스
            continue
        for i in graph[now]:# 연결된 노드 탐색
            cost = dist + i[1]# 현재 노드의 최단거리 + 다음 노드까지의 거리
            if cost < distance[i[0]]:# 다음노드의 최단거리보다 구한cost가 더 작으면
                distance[i[0]] = cost# 다음 노드의 최단거리를 업데이트
                heapq.heappush(q,(cost,i[0]))# 힙에 다음노드에 대한 최단거리, 노드 넣어줌



INF = int(1e9)
v,e,k,start = map(int, input().split(" "))
graph = [[] for i in range(v+1)]
distance = [INF]*(v+1)

for i in range(e):
    a,b = map(int,input().split(" "))
    c = 1 # 편의를 위해 거리1을 강제로 넣어줌
    graph[a].append((b,c))

dijkstra(start)

res = []
for i in range(len(distance)):
    if distance[i] == k: # 특정거리인 경우 출력하고 res에 넣어줌
        print(i)
        res.append(i)
if res == []: # res에 아무것도 없으면
    print(-1)

