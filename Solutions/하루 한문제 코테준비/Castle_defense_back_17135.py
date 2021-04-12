import math
import copy

died = []
def dist(r1,c1,r2,c2): # 거리구하는 함수
    return abs(r1-r2)+abs(c1-c2)

def shoot(graph,ach_row,ach_col):
    count_list =[]
    global died # 죽인 리스트

    for i in range(ach_row-1 ,-1, -1): # 궁수의 위치 -1 행부터 0까지
        for j in range(m): # 모든 열 탐색
            if graph[i][j] == 1: # 해당노드가 몬스터이면
                length = dist(ach_row,ach_col,i,j) # 궁수와 몬스터 거리 구하고
                if length <= d: # 거리보다 작으면
                    count_list.append((length,j,i)) # 거리,몬스터위치추가 # i,j위치를 바꿔야 왼쪽부터 선택한다는 조건 만족함
                                                    # sort하면 첫번째비교, 두번째비교 '''이렇게 순차적으로 비교된다.
    if count_list: # 거리안에 쏠수 있는 게 있으면
        count_list.sort() # 제일 거리 가까운거 찾기 위해
        died.append((count_list[0][2],count_list[0][1])) # 죽인 리스트에 제일 거리 가까운거 넣음
        return True
    else: # 쏠수 있는게 없으면 False
        return False

n,m,d = map(int, input().split(" "))

graph = []
for i in range(n):
    graph.append(list(map(int,input().split(" "))))


sc = 0 # 몇번 쐈는지 카운트하는 변수
real_result = 0 # 최종 값
for i in range(m-2):
    for j in range(i+1,m-1):
        for e in range(j+1,m): # 3개 선택할수 있는 모든 경우의 수
            result = 0 # 턴 당 죽인 몬스터 수
            copy_graph = copy.deepcopy(graph) # 카피리스트
            for r in range(n,0,-1): # 궁수의 행 위치가 턴당 위로 올라감
                for c in [i,j,e]: # 궁수의 세가지 열의 위치
                    if sc < 3: # 세번보다 덜 쐈으면
                        if shoot(copy_graph,r,c): # 궁수의 위치보다 한칸위 부터 쏠수있는 몬스터 탐색한다음 제일 작은거 died에 넣음
                            sc += 1 # 한번 쐈음

                sc = 0 #다음턴을 위한 초기화
                for enemy in died: # 화살을 쏜 위치 (중복된 위치 일 수도)
                    if copy_graph[enemy[0]][enemy[1]] == 1: # 화살을 쏜 위치에 몬스터가 있으면
                        result += 1 # +1
                        copy_graph[enemy[0]][enemy[1]] = 0 # 0으로 만들어서 한번 죽인 몬스터가 중복 카운트 되지 않게
                died.clear()

            real_result = max(real_result,result)


print(real_result)
