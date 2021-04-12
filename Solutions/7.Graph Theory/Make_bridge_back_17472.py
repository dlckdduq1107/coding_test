
def find_parent(x): # 조상 찾기
    if parent[x] != x: # 자신의 부모가 자신과 다르면 더 거슬러간다는 소리
        parent[x] = find_parent(parent[x]) # 재귀역할
    return parent[x]

def union_parent(a,b): # 합집합
    a = find_parent(a) # a의 조상찾기
    b = find_parent(b) # b의 조상 찾기
    if a < b: # a가 더 작으면
        parent[b] = a # b를 a에 연결
    else: # b가 더 작으면
        parent[a] = b # a를 b에 연결

def dfs(graph,i,j):
    if graph[i][j] == 1: # 1이면
        graph[i][j] = island # 라벨링
        is_number[island] = 1 # 섬번호를 딕셔너리에 넣어줌

        for q in range(4): # 4방향 모두 탐색
            if (0<= i+dx[q] < row) and(0<= j+dy[q] < col): # 범위 안벗어나고
                if graph[i+dx[q]][j+dy[q]] == 1: # 탐색한게 1이면
                    dfs(graph,i+dx[q],j+dy[q])

island = 2 # 섬번호를 표시하기 위한 변수
is_number = {} # 섬 번호만을 담기 위한 딕셔너리
row,col = map(int, input().split(" "))
graph = []
edge = [] # (cost,시작,끝)을 담을 리스트
parent = [0]*1000 # 넉넉하게 1000으로 잡음
for i in range(1000): # 자기자신 초기화
    parent[i] = i

dx = [0,0,1,-1] # 4방향
dy = [1,-1,0,0]

for i in range(row): # 배열 입력을 2차원 그래프로 변환
    graph.append(list(map(int,input().split(" "))))

for i in range(row): # dfs를 통해 각각 섬번호를 라벨링해줌
    for j in range(col): # 하나하나 모두 탐색
        dfs(graph,i,j)
        island += 1 # 섬번호를 다르게 해주기 위한 +=

for i in range(row):
    for j in range(col): # 전체 탐색
        if graph[i][j] != 0: # 섬 발견하면
            for q in range(4): # 4방향 탐색
                count = 0 # 다른 섬으로 가기위한 길이 변수
                nx = i+dx[q] # 다음방향
                ny = j+dy[q]

                if 0<= nx < row and 0<= ny < col: # 다음탐색 위치가 범위안에 있고
                    if graph[nx][ny] == graph[i][j]: # 현재 섬번호랑 같으면 같은 섬 탐색이므로 패스
                        continue
                    if graph[nx][ny] == 0: # 0이면
                        nnx,nny = nx,ny # 한방향으로 탐색해나갈 변수 설정
                        while 0<=nnx<row and 0<=nny<col and graph[nnx][nny] == 0: # 범위 안에 있고, 해당 값이 0일 동안(다른 섬에 도착할 동안) 반복
                            count += 1 # 길이 +=
                            nnx = nnx+dx[q] # 특정 방향으로 계속 갈수 있도록 다음 위치 설정
                            nny = nny+dy[q] # 특정 방향으로 계속 갈수 있도록 다음 위치 설정
                        if 0<=nnx<row and 0<=nny<col: # 범위 안에 있다면(해당 값이 0이 아니어서<다른 섬에 도달>) 엣지 추가
                            edge.append((count,graph[i][j],graph[nnx][nny])) # (길이,시작,도착)
                        else: # 범위를 벗어나 while을 빠져나온 경우
                            continue

# print(graph)


edge.sort() # 길이를 기준으로 정렬
# print(edge)
result = 0
for cost,x,y in edge:
    if cost == 1: # 거리가 1이면 패스
        continue
    if find_parent(x) != find_parent(y): # 부모가 다르면 합쳐준다.
        union_parent(x,y)
        result += cost # 거리를 더해줌

# print(parent)
for i in range(1000): # 특정 노드가 부모로 안되어 있는 경우도 있어서 한번더 부모 노드를 바꿔줌(다 잘바꼈는지 체크 하는 역할)
    find_parent(i) # 모든 부모노드 확인해줌
# print(parent)
# print(is_number)

# min_node = 10000 ## 제일 먼저 번호가 매겨진 섬 번호 구하기
# for i in graph:
#     for j in i:
#         if j != 0:
#             if j < min_node:
#                 min_node = j

min_node = min(is_number.keys()) # 제일 먼저 번호가 매겨진 섬 리턴(유니온 파인드 결과 제일 작은 노드가 최종 부모로 설정 되므로)
# print(min_node)
for i in is_number.keys(): # 섬번호가 매겨진 것만 탐색
    if parent[i] != min_node: # 섬번호가 매겨진 것 중에 최종 부모노드(min_node)로 연결되어있지 않으면 연결 안된것임
        print(-1)
        exit(0) # 프로그램 종료
print(result)

