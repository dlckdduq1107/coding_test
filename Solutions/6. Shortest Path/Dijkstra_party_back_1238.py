import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 자기자신은 0으로
    distance[start] = 0

    while q:  # 우선순위 큐 사용
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 최단거리가 더 작으면 이미 확정이므로 패스
            continue
        for i in graph[now]:  # 연결된 노드 탐색
            cost = dist + i[1]  # 현재 노드의 최단거리 + 다음 노드까지의 거리
            if cost < distance[i[0]]:  # 다음노드의 최단거리보다 구한cost가 더 작으면
                distance[i[0]] = cost  # 다음 노드의 최단거리를 업데이트
                heapq.heappush(q, (cost, i[0]))  # 힙에 다음노드에 대한 최단거리, 노드 넣어줌
INF = int(1e9)
v,e,end = map(int,input().split(" "))
graph = [[] for i in range(v+1)]

for i in range(e):
    a,b,c = map(int, input().split(" "))
    graph[a].append((b,c))

result = 0
for i in range(1,v+1):
    res = 0
    #시작 - 끝 다익스트라 한번
    distance = [INF] * (v + 1)
    dijkstra(i)
    res += distance[end]
    # 끝 - 시작 다익스트라 두번
    distance = [INF] * (v + 1)
    dijkstra(end)
    res += distance[i]

    if res > result:
        result = res

print(result)