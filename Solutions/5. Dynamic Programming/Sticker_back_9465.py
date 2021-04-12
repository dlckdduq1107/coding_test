
case = int(input())

for i in range(case): # 케이스만큼 반복
    result = []
    n = int(input())
    cost = []
    cost.append(list(map(int,input().split(" "))))
    cost.append(list(map(int, input().split(" ")))) # 입력 리스트화

    cost[0][1] += cost[1][0] #두번째줄 업데이트
    cost[1][1] += cost[0][0]

    for j in range(2,n): # 인덱스 2부터 n까지 반복
        cost[0][j] = max(cost[1][j-1],cost[1][j-2])+cost[0][j] # 왼쪽 대각선과 왼쪽 두번째 대각선비교
        cost[1][j] = max(cost[0][j-1],cost[0][j-2])+cost[1][j]

    print(max(max(cost[0]),max(cost[1]))) # 리스트중 제일 큰 값 출력




