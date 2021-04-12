n = int(input())
length = list(map(int, input().split(" ")))
cost = list(map(int, input().split(" ")))

res = int(1e9) # 최종적인 가격
pivot = int(1e9) # 지나오면서 가장 싼 기름값을 저장할 변수
for i in range(n-1): # 마지막 노드이전까지 탐색
    if i == 0: # 첫번째는 무조건 기름을 충전해야 하므로 예외처리
        pivot = cost[i] # 가장 작은 값을 맨처음의 기름값으로 세팅
        res = length[i]*cost[i] # 최종값을 처음기릅값*처음 거리로 세팅
    else: # 두번째 부터
        pivot = min(pivot,cost[i]) # 기록된 값보다 작으면 선택, 아니면 그대로
        res += pivot*length[i] # 가장 작은 기름값에 대한 거리를 곱해줌


print(res)