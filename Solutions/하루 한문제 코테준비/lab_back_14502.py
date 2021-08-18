import copy
def count_safe(temp_graph):# 안전지역 개수를 세는 함수(count함수 이용하면 빠름)

    return sum(i.count(0) for i in temp_graph)

def select_wall(start,count):# 벽을 선택하는 함수 모든 경우 탐색(조합)
    global max_safe # 최대 안전지역 개수
    if count == 3: # 벽을 3개 설정했을때
        temp_graph = copy.deepcopy(graph) # 다른 경우도 탐색해야되니까 deepcopy
        for i in range(n): # 그래프의 모든 부분 탐색
            for j in range(m):
                if(temp_graph[i][j] == 2): # 바이러스가 있는 경우에만 바이러스 퍼뜨림
                    spread_virus(temp_graph,i,j)
        max_safe = max(max_safe,count_safe(temp_graph)) # 바이러스 퍼뜨린 다음 안전지역 개수 카운트

    else: # 아직 벽을 3개 설정하지 않았을때
        for i in range(n*m): # 모든 경우의 수 탐색
            x = i//m # 행
            y = i%m # 열
            if(graph[x][y] == 0): # 해당 부분이 빈 공간 일때
                graph[x][y] = 1 # 벽을 세우고
                select_wall(start,count+1) # 재귀
                graph[x][y] = 0 # 원래상태로 되돌림

def spread_virus(temp_graph,x,y): # 바이러스 퍼뜨리는 함수
    for i in range(4): # 네방향을 돌면서
        nx = x+dx[i]
        ny = y+dy[i]
        if(0<=nx<n and 0<=ny<m and temp_graph[nx][ny] == 0): # 빈공간이면
            temp_graph[nx][ny] = 2 # 바이러스 퍼드림
            spread_virus(temp_graph,nx,ny) # 퍼뜨린 공간에서부터 다시 퍼뜨림





n,m = map(int, input().split(" "))
graph = []
max_safe = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    graph.append(list(map(int,input().split(" "))))


select_wall(0,0)
print(max_safe)


