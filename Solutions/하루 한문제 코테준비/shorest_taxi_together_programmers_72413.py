import heapq
def dijkstra(n,start, graph):
    distance = [int(1e9) for i in range(n+1)]

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

    return distance # 거리 리스트 리턴



def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph = [[] for i in range(n+1)]
    for q,w,e in fares:
        graph[q].append((w,e))
        graph[w].append((q,e))

    distance = dijkstra(n,s,graph)
    answer = distance[a]+distance[b] # 시작점에서 A,B까지의 거리 합

    for i in range(1,n+1): # 합승 지점부터 A,B까지의 거리 구하기
        if(i==s):
            continue
        else:
            dist = dijkstra(n,i,graph) # 합승지점(시작)부터 최단거리
            answer = min(answer,dist[a]+dist[b]+distance[i]) # 합승지점+A,B각각까지의 거리

    return answer


# print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))