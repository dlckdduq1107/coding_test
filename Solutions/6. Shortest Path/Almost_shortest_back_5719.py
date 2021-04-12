import heapq
from collections import deque
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

def remove(): # BFS를 이용하여 최단거리 경로를 제거해줌(end에서 start까지 탐색한다고 생각) # visited는 넣어줄 필요가 없음(visted를 넣으면 한번 갔던 곳은 다시 안가게 되므로 노드가 중복되는 최단경로에서 한개의 경로밖에 삭제하지 않게됨
    q = deque([end])

    while q:
        node = q.popleft()
        if node == start: # 시작이랑 같으면 넘어감(끝에 다 온것 이므로) #없어도 정답 판정 받음
            continue
        for pre,charge in graph_reverse[node]: # 역추적 리스트에 BFS적용
            if distance[pre] + charge == distance[node]: # 이전 최단거리 + 웨이트 == 현재 최단거리이면 최단거리는 이전 노드에서 온것임
                if (node,charge) in graph[pre]: # 삭제한거 또 삭제할 수 있으므로 중복체크해야함
                    graph[pre].remove((node,charge)) # 원래 그래프 리스트에서 역추적한 최단거리 경로 삭제
                    q.append(pre) # 다음꺼 탐색위해 큐에 넣어줌

    # if end != start: # 재귀함수를 이용해도됨 (중복체크 해줘야함) # 함수 파라미터도 추가해줘야함
    #     for i in graph_reverse[end]:
    #         if distance[end] == distance[i[0]] + i[1]:
    #             if (end,i[1]) in graph[i[0]]:
    #                 graph[i[0]].remove((end, i[1]))
    #                 remove(i[0])


INF = int(1e9)
while True:
    v, e = map(int, input().split(" "))
    if v == 0 and e == 0:
        break
    start, end = map(int, input().split(" "))
    graph = [[] for i in range(v)]
    graph_reverse = [[] for i in range(v)] # 역추적을 위해 리버스 리스트 만들어줌
    distance = [INF]*v
    visited = [False] * v   # 방문표시
    for i in range(e):
        a,b,c = map(int, input().split(" "))
        graph[a].append((b,c))
        graph_reverse[b].append((a, c)) # 역추적 위한 리스트에 추가

    dijkstra(start) # 다익스트라로 최단거리 구함

    remove() # 최단거리 경로 제거
    distance = [INF]*v # 다익스트라 다시 반복
    dijkstra(start)

    if distance[end] == INF:
        print(-1)
    else:
        print(distance[end])







