import copy
def rotate(direct):
    if direct == 0: # 오른쪽 회전
        for i in range(n):
            idx = n-1 # idx를 맨끝으로 놓고
            for j in range(n-2,-1,-1): # 맨끝에서 두번째 부터 탐색
                if graph[i][j]: # 0이 아닌경우에만
                    temp = graph[i][j] # 임시저장하고
                    graph[i][j] = 0 # 현재 값 0 으로 세팅
                    if graph[i][idx] == 0: # idx값이 0이면
                        graph[i][idx] = temp # 임시저장한거를 넣어준다.
                    elif graph[i][idx] == temp: # idx값이 임시저장과 같으면
                        graph[i][idx] = temp*2 # idx자리에 *2해서 넣어주고
                        idx -= 1 # idx는 한칸 앞으로 간다.
                    else: # 0도 아니고 임시저장과 같지도 않으면
                        idx -= 1 # 현재 idx값은 바뀔여지가 없으므로 idx한칸 앞으로
                        graph[i][idx] = temp # 0으로 만든값 다시 처음상태로 저장(2 0 4 같은 경우는 앞에서 처리되어서 안옴) 여기서는 2 4와 같이 인접했을때 숫자 다른경우만 옴

    elif direct == 1: # 왼쪽
        for i in range(n):
            idx = 0
            for j in range(1,n):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][idx] == 0:
                        graph[i][idx] = temp
                    elif graph[i][idx] == temp:
                        graph[i][idx] = temp*2
                        idx += 1
                    else:
                        idx += 1
                        graph[i][idx] = temp
    elif direct == 2: #아래쪽
        for j in range(n):
            idx = n-1
            for i in range(n-2,-1,-1):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[idx][j] == 0:
                        graph[idx][j] = temp
                    elif graph[idx][j] == temp:
                        graph[idx][j] = temp*2
                        idx -= 1
                    else:
                        idx -= 1
                        graph[idx][j] = temp
    elif direct == 3: # 위쪽
        for j in range(n):
            idx = 0
            for i in range(1,n):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[idx][j] == 0:
                        graph[idx][j] = temp
                    elif graph[idx][j] == temp:
                        graph[idx][j] = temp*2
                        idx += 1
                    else:
                        idx += 1
                        graph[idx][j] = temp


def dfs(cnt):
    global graph, result
    if cnt == 5: # 총 5번 이동
        for i in graph:
            for j in i:
                result = max(result,j)

        return


    for i in range(4): # 4방향으로 이동
        temp_graph = copy.deepcopy(graph) # 이전 상태 저장
        rotate(i)  # 회전
        dfs(cnt+1) # +1해서 dfs
        graph = copy.deepcopy(temp_graph) # 상태 되돌리기





n = int(input())

graph = []
result = 0
for i in range(n):
    graph.append(list(map(int, input().split(" "))))


dfs(0)
print(result)


