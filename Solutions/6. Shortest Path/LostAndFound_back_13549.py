import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 자기자신은 0으로
    distance[start] = 0

    while q: # 우선순위 큐 사용
        dist,now = heapq.heappop(q)
        if distance[now] < dist: # 최단거리가 더 작으면 이미 확정이므로 패스
            continue
        for i in [now-1,now+1]: # 한칸전, 한칸뒤 탐색
            if 0<= i <= end*2: # 범위안에 있는지 판단
                cost = dist+1
                if cost < distance[i]: # +1한게 더 작으면 갱신
                    distance[i] = cost
                    heapq.heappush(q,(cost,i))

        if now*2 <= end*2: # *2칸이 범위안에 있을때
            if dist < distance[now*2]: # 현재 최단거리가 더 작을때, 순간이동 이므로 여기서는 +1을 안해줌
                distance[now*2] = dist
                heapq.heappush(q,(dist,now*2))

INF = int(1e9)
start,end = map(int, input().split(" "))
distance = [INF]*(end*2+1)

if start > end: # 시작이 더 높을때 예외처리
    print(start-end)
else: # 이외의 경우
    dijkstra(start)
    print(distance[end])