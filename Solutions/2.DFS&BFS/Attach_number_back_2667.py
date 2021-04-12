def dfs(graph,i,j,pivot):
    if graph[i][j] == 1:
        graph[i][j] += 1 # 값을 +해주어 1이 아니게 만들어줌
        if pivot in total_num: # 각각 개수를 세기 위한 설정
            total_num[pivot] += 1
        else:
            total_num[pivot] = 1

        for q in range(4): # 4방향 모두 탐색
            if (0<= i+dx[q] < n) and(0<= j+dy[q] < n): # 범위 안벗어나고
                if graph[i+dx[q]][j+dy[q]] == 1: # 탐색한게 1이면
                    dfs(graph,i+dx[q],j+dy[q],pivot)


n = int(input())
graph = []

for i in range(n): # 입력을 이차원 리스트로 변환
    graph.append(list(map(int,input())))

dx = [0,0,1,-1] # 네방향 추적을 위한 리스트
dy = [1,-1,0,0]

pivot = 0 # 총 개수를 세기위한 피벗
total_num ={} # 총개수와 각 개수를 세기위한 딕셔너리

for i in range(n):
    for j in range(n): # 그래프의 각 요소 모두 탐색
        if graph[i][j] == 1: # 1이면 탐색 시작이므로 총개수를 위한 피벗 +1
            pivot += 1
        dfs(graph,i,j,pivot)

total_num = dict(sorted(total_num.items(), key=lambda x: x[1])) # 값을 기준으로 딕셔너리 정렬

print(len(total_num))
for i in total_num:
    print(total_num[i])
