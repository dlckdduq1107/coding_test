import copy
n = int(input())

graph = []
for i in range(n): # 입력값을 그래프로 표현
    graph.append(list(map(int,input().split(" "))))

cost = copy.deepcopy(graph) # 비용을 기록하기 위한 리스트 카피
for i,q in enumerate(cost): # 0으로 초기화
    for j,w in enumerate(q):
        cost[i][j] = 0
cost[0][0] = graph[0][0] # 처음 노드만 초기화 시켜줌
# print(graph)
# print(cost)

for i,q in enumerate(cost):
    if i == n-1: # 마지막노드도 실행하면 다음인덱스가 없어서 에러남, 마지막 줄에 도달하면 빠져나감
        break
    for j,w in enumerate(q): # 모든 노드 탐색
        c = cost[i][j] + graph[i+1][j] # 대각선왼쪽아래 탐색
        if c > cost[i+1][j]: # 만약 값이 더 크면 업데이트
            cost[i + 1][j] = c

        c2 = cost[i][j] + graph[i + 1][j+1] # 대각선 오른쪽 아래 탐색
        if c > cost[i + 1][j+1]: # 값이 더 크면 업데이트
            cost[i + 1][j+1] = c2

print(max(cost[n-1])) # 마지막 줄에서 가장 큰 값 출력
