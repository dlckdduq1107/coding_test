import copy
import sys
sys.setrecursionlimit(10**6)

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

def dfs(graph,land,i,j,pivot,row,col,height):
    if graph[i][j] == 0:
        graph[i][j] = pivot # 번호매기기
        is_number[pivot] = 1 # 번호매긴거 딕셔너리에 넣어줌

        for q in range(4): # 4방향 모두 탐색
            if (0<= i+dx[q] < row) and(0<= j+dy[q] < col): # 범위 안벗어나고
                if graph[i+dx[q]][j+dy[q]] == 0 and abs(land[i+dx[q]][j+dy[q]]-land[i][j]) <= height: # 탐색한게 0이고 높이보다 작으면
                    # if visited[i+dx[q]][j+dy[q]] == 0: # 아직 방문 안했으면
                    dfs(graph,land,i+dx[q],j+dy[q],pivot,row,col,height)

def cost_check(row,col,graph,land):
    for i in range(row):
        for j in range(col): # 모든 노드 탐색
            for q in range(4): # 4방향 탐색
                if (0 <= i + dx[q] < row) and (0 <= j + dy[q] < col):  # 범위 안벗어나고
                    if graph[i + dx[q]][j + dy[q]] != graph[i][j] and graph[i + dx[q]][j + dy[q]] != 0: # 아직 탐색안한부분빼고, 현재와 같은 피봇 말고
                        res = abs(land[i][j]-land[i + dx[q]][j + dy[q]]) # 인접된 영역에서의 최솟값
                        edge.append((res,graph[i][j],graph[i + dx[q]][j + dy[q]]))

def solution(land, height):
    global is_number
    is_number = {}
    global edge
    edge = []  # (cost,시작,끝)을 담을 리스트
    global parent
    parent = [0] * 100000  # 300x300이므로 넉넉하게 십만
    for i in range(100000):  # 자기자신 초기화
        parent[i] = i
    global dx,dy

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = 0
    row = len(land)
    col = len(land[0])
    pivot = 0
    graph = copy.deepcopy(land)

    for i,v in enumerate(graph):
        for j in range(len(v)):
            graph[i][j] = 0
    # print(graph)
    for i in range(row):
        for j in range(col): # 모두 탐색
            if graph[i][j] == 0: # 아직번호 안매긴 상태이면
                pivot += 1
                dfs(graph,land,i,j,pivot,row,col,height) # 영역별 번호 매기기

    cost_check(row,col,graph,land) # 모든 노드 탐색하여 (비용,시작,끝)요소 추가하기
    edge.sort() # 비용 작은거 부터 정렬
    for cost,x,y in edge: # 유니온 파인드
        if find_parent(x) != find_parent(y):
            union_parent(x,y)
            answer += cost

    return answer

land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]#[[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = int(input())
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

print(solution(land,height))