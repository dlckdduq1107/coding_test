import copy
def select(games):# 최대로 볼수 있는 경기개수 카운트 하는 함수
    global max_count
    current_time = 0 # 현재시간
    for i in games: # 게임을 반복하면서
        if(current_time <= i[1]): # 현재 시간이 경기시작시간보다 작으면 경기관람가능
            max_count += 1 # 카운트 ++
            current_time = i[2] # 현재시간을 경기끝나는 시간으로 업데이트


n = int(input()) # 케이스 숫자
for i in range(n):
    max_count = 0 # 최대 경기 관람수
    case = int(input()) # 입력숫자
    game = [] # 전체 게임 입력 리스트
    split_games = [] # 날짜별로 나뉘어있는 게임 리스트
    for j in range(case): # 모든 게임 입력
        game.append(list(map(int, input().split(" "))))

    game.sort(key=lambda x:x[0]) # 첫번째를 기준으로 게임 정렬(날짜별)

    pivot = game[0][0] # 현재 날짜
    temp = [] # 날짜별 게임 리스트를 담을 임시 리스트
    for j,g in enumerate(game): # 정렬된 모든 게임리스트 돌면서
        if(j == len(game)-1): # 마지막이면 해당날짜 게임 리스트추가
            temp.append(g)
            split_games.append(temp)
            break
        if(pivot == g[0]): # 현재 피벗과 같으면 임시에 계속 추가
            temp.append(g)
        else: # 현재 피벗과 다르면
            split_games.append(temp) # 이전날짜꺼 추가하고
            temp = [] # 임시 리스트 초기화
            temp.append(g) # 현재날짜의 제일 처음꺼 추가
            pivot = g[0] # 피벗 업데이트


    for g in split_games: # 날짜별로 나뉘어진 게임 리스트를 돌면서
        temp_game = copy.deepcopy(g) # 딥카피
        temp_game.sort(key=lambda x:x[2]) # 경기 끝나는 시간으로 정렬
        select(temp_game) # 관람가능 경기수 함수 실행

    ###출력부분###
    #print(game)
    #print(split_games)
    print("Scenario #"+str(i+1)+":")
    print(max_count)
    print()