import heapq
def check_left(x,y): # 왼->오 탐색
    if y == 0: # 첫번째 항은 위에서 그대로 가져와 더해줌
        left[x][y] = distance[x-1][y]+graph[x][y]
    else: # 두번째 항부터는 위와 왼쪽중 최댓값을 선택
        left[x][y] = max(left[x][y-1], distance[x-1][y]) + graph[x][y]

def check_right(x,y): # 오->왼 탐색
    if y == col-1: # 맨 끝쪽이면 위에서 그대로 가져옴
        right[x][y] = distance[x-1][y]+graph[x][y]
    else: # 다음항부터는 위, 오른쪽중 최댓값을 선택
        right[x][y] = max(right[x][y+1], distance[x-1][y]) + graph[x][y]



INF = int(1e9)
row,col = map(int, input().split(" "))
graph = []
for i in range(row): # 입력의 리스트화
    graph.append(list(map(int,input().split(" "))))

distance = [[-INF for i in range(col)] for j in range(row)] # 최종거리 리스트
left = [[-INF for i in range(col)] for j in range(row)] # 왼->오 탐색 리스트
right = [[-INF for i in range(col)] for j in range(row)] # 오->왼 탐색 리스트


for i in range(col): # 첫번째항 초기화
    if i == 0:
        distance[0][0] = graph[0][0]
        left[0][0] = graph[0][0]
        right[0][0] = graph[0][0]
    else:
        distance[0][i] = distance[0][i-1] + graph[0][i]
        left[0][i] = left[0][i - 1] + graph[0][i]
        right[0][i] = right[0][i - 1] + graph[0][i]


for i in range(1,row): # 2번째 행부터 실행
    for j in range(col): # 행별 각각의 노드마다 좌우, 우좌 탐색 실행
        check_left(i,j)
        check_right(i,col-j-1)
    for j in range(col): # 위에서 실행된 값중에 큰 값을 선택
        distance[i][j] = max(left[i][j],right[i][j])


print(distance[row-1][col-1])
