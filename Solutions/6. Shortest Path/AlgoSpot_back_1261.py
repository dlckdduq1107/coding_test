import heapq
def dijkstra(row, col):
    q = []
    heapq.heappush(q, (0, row,col))  # 자기자신은 0으로
    distance[row][col] = 0
    visited[row][col] = True # 시작점 방문 표시

    while q:  # 우선순위 큐 사용
        dist, now_r, now_c = heapq.heappop(q)
        # if distance[now_r][now_c] < dist:  # 최단거리가 더 작으면 이미 확정이므로 패스 # 0일경우 거리가 늘어나지 않아 필요없는 부분
        #     continue
        for i in range(4):  # 상하좌우 탐색
            x = now_r+dx[i]
            y = now_c+dy[i]

            if 0<= x < m and 0<= y <n: # 범위안에서 탐색
                if visited[x][y] == True: # 방문 했었으면 패스(이전꺼 다시 탐색할 경우 막아줌)
                    continue

                if graph[x][y] == 0: # 탐색한 부분이 0이면 이전꺼를 그대로 가져온다
                    cost = distance[now_r][now_c]
                    if cost < distance[x][y]: # 이전꺼 그대로 가져온것이 현재 최소깨기보다 작으면 업데이트 해준다.
                        distance[x][y] = cost # 업데이트
                        visited[x][y] = True # 방문 표시

                elif graph[x][y] == 1: # 탐색한 부분이 1이면 이전꺼 +1 을 해준다.
                    cost = distance[now_r][now_c] + 1
                    if cost < distance[x][y]: # 이전꺼 +1이 현재 최소깨기 보다 작으면 업데이트 해준다.
                        distance[x][y] = cost # 업데이트
                        visited[x][y] = True # 방문표시

                heapq.heappush(q,(cost,x,y)) # 다음노드 큐에 넣어줌(cost는 넣어줄 필요 없는 것 같음 - 사용하지 않음)


n,m = map(int,input().split(" "))
INF = int(1e9)
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited =[[False]*n for i in range(m)] # [[False]*n]*m하면 내부가 복사되어서 하나만 수정해도 다 수정됨
distance = [[INF]*n for i in range(m)]

for i in range(m): # 입력 2차원 리스트화
    graph.append(list(map(int,input())))

dijkstra(0,0)

print(distance[m-1][n-1])