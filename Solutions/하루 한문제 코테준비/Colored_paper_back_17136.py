def dfs(dep): # dep은 여태까지 구한 색종이의 개수를 의미한다.
    global result,total_one # 최종개수, 그래프에서 1의개수

    if result > 0 and result <= dep: # result가 한번 업데이트 되고, 구한개수(dep)보다 현재개수(result)가 더 작을때 업데이트 안함
        return

    if total_one == 0: # 그래프를 색종이로 다 채웠을때
        if result == -1: # 맨처음으로 업데이트 될때
            result = dep # 구한 개수로 업데이트
        else: # 맨처음 업데이트 이후
            result = min(result,dep) # 개수가 작은거를 매번 선택

    for i in range(10): # 제일 처음 나오는 1의 위치를 구하기
        for j in range(10):
            if graph[i][j] == 1: # 1이면 나가고
                break
        if graph[i][j] == 1: # 1이면 나가서 i,j에 1의 위치가 들어감
            break

    if graph[i][j] == 1: # 현재 위치가 1일때
        for size in range(1,6): # 1~5까지 크기의 색종이를 붙여봄
            if limit_list[size-1] != 0: # 각 색종이 제한이 안넘을때
                location = [] # 위치를 기록할 리스트
                if check(i,j,size): # 해당 사이즈로 덮을수 있을때
                    for _i in range(i, i + size): # 0으로 바꾸고 위치를 기록
                        for _j in range(j, j + size):
                            graph[_i][_j] = 0
                            location.append((_i,_j))

                    total_one -= size**(2) # 0으로 바꾼만큼 1의총 개수를 줄여줌
                    limit_list[size-1] -= 1 # 색종이를 하나 사용했으므로 색종이 제한 -1

                    dfs(dep+1) # 색종이 하나를 더붙였으므로 +1하고 재귀로 돌려줌

                    #0으로 바꿨던 것들을 초기화 시켜줌
                    total_one += size ** (2)
                    limit_list[size - 1] += 1
                    for x,y in location:
                        graph[x][y] = 1

def check(x,y,dep): # 해당 위치의 뎁스를 확인하는 함수
    for i in range(x,x+dep): # 뎁스만큼 반복
        for j in range(y,y+dep):
            if not (0 <= i < 10 and 0<= j < 10):
                return False
            if graph[i][j] != 1: # 1이 아니면 정사각형이 하나라도 안채워져있으므로 Flase
                return False
    return True # 다 1로 채워져있으면 True

graph = []
for i in range(10): # 인풋
    graph.append(list(map(int,input().split(" "))))

# copy_graph = [[0 for i in range(10)] for j in range(10)]
# location = [] # 위치 기록
# max_dep = 0 # 최대 dep
limit_list = [5,5,5,5,5] # 각자 색종이 개수의 제한
result = -1 # 최종개수
total_one = 0 # 1의개수
for i in graph: # 1의 개수를 카운트
    total_one += sum(i)

dfs(0) # 개수가 0부터 시작
print(result)








# def check_copy(x,y,dep): # 해당 위치 뎁스에 대한 체크 함수
#     for i in range(x,x+dep): # 뎁스만큼 반복
#         for j in range(y,y+dep):
#             if not (0 <= i < 10 and 0 <= j < 10):
#                 return False
#             if copy_graph[i][j] == 0: # 0이면 모두 채워져있지 않으므로 False(실제로는 다 채워져있는데 다른 숫자로 채워져있는 경우도 있으므로 0이 아닐때는 모두 채워져 있다고 판단)
#                 return False
#     return True # 다 dep 로 채워져있으면 True

# def fill(x,y,dep,to_one): # copy를 dep으로 채우는 함수
#     for i in range(x, x + dep):  # 뎁스만큼 반복
#         for j in range(y, y + dep):
#             if to_one:
#                 graph[i][j] = 0 # dep을 채움
#             else:
#                 graph[i][j] = 1


# def blanc(x,y,dep): # dep에 따라 요소들을 0으로 만들어주는 함수
#     for i in range(x, x + dep):  # 뎁스만큼 반복
#         for j in range(y, y + dep):
#             if not (0 <= i < 10 and 0 <= j < 10): # 범위 예외처리
#                 continue
#             copy_graph[i][j] = 0
#             # location.remove((i,j))

# for i in range(10): # 완전 탐색으로 색종이를 채울수 있는 가장 큰 dep으로 copy를 채움
#     for j in range(10):
#         for depth in range(5,0,-1): # dep가 큰 거 부터 할당시작
#             if check(i,j,depth): # dep만큼의 요소가 꽉 차 있으면
#                 fill(i,j,depth) # dep의 값을 채우고 밑의 숫자는 안채워도 됨
#                 break
#
# # for i in copy_graph:
# #     print(i)
# # print(max_dep)
#
#  # 열, 행 순서로 정렬
# # location.sort(key=lambda x:x[1])
# # location.sort(key=lambda x:x[0])
# # print(location)
#
# count = 0 # 최종 색종이 개수
# for dep_check in range(max_dep,0,-1): # 5부터 1까지 탐색
#     for i,j in location: # 기록된 위치만 확인
#         if copy_graph[i][j] == dep_check and check_copy(i,j,dep_check) and limit_list[dep_check-1] > 0: # 해당 위치가 dep과 같고 없앨수 있게 꽉차있는지, 색종이 다 안썼으면
#             blanc(i,j,dep_check) # dep에 해당하는 위치 모두 지우기
#             count += 1 # 개수 카운트
#             limit_list[dep_check-1] -= 1 # 색종이 개수 -1
#             print(count)
#             for q in copy_graph:
#                 print(q)
#             print()
#
# for i,j in location: # 기록된 위치
#     if copy_graph[i][j] != 0 and limit_list[0] > 0: # 0이 아니고,1x1색종이 개수가 남았을때
#         count += 1 # 색종이 카운트
#         copy_graph[i][j] = 0 # 해당 요소 0으로
#         limit_list[0] -= 1 # 제한 개수 -1
#
#
# for i in copy_graph:
#     print(i)
#
# for i,j in location: # 위치 검사
#     if copy_graph[i][j] != 0: # 0으로 안바뀐 곳이 있으면
#         print(-1) # 예외처리
#         exit(0)
#
# print(count)
#
# ###에외케이스 해결하기
#
