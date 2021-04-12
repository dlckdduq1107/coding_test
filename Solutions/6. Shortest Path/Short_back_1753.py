import heapq
def dijkstra(start):
    q = [] # 힙 사용하기 위한 리스트
    heapq.heappush(q,(0,start)) # 처음과의 최단거리는 0으로 하고 우선순위 큐에 넣어줌
    distance[start] = 0 # 자신과의 거리가 0이 되게함
    while q: # 큐가 다 빌때 가지
        dist, now = heapq.heappop(q) # 현재 위치에 대한 최단거리와 노드를 pop
        if distance[now] < dist: # 이미 구해진 거리가 더 작을때는 판단 할 필요 없음(하나하나씩 최단거리를 확정하는거이기 때문)
            continue
        for i in graph[now]: # 현재 노드에 연결된 모든 노드 확인
            cost = dist + i[1] # 현재 노드의 최단거리 + 다음 노드까지의 거리
            if cost < distance[i[0]]: # 다음노드의 최단거리보다 구한cost가 더 작으면
                distance[i[0]] = cost # 다음 노드의 최단거리를 업데이트
                heapq.heappush(q,(cost,i[0])) # 힙에 다음노드에 대한 최단거리, 노드 넣어줌

INF = int(1e9) # 무한대값을 표현
v,e = map(int,input().split(" "))
start = int(input())

graph = [[] for i in range(v+1)] # 그래프 처음은 비워둠
distance = [INF]*(v+1) # 거리를 무한대로 초기화

for i in range(e): # 엣지와 웨이트를 그래프에 넣어줌
    a,b,c = map(int, input().split(" "))
    graph[a].append((b,c))

dijkstra(start) # 다익스트라 실행

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

