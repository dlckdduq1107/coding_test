n,k = map(int, input().split(" "))

bag = [[0 for i in range(k+1)] for j in range(n+1)] # 물건의 개수와 제한 중량 만큼 리스트 생성
cost_val = [[0,0]] # 물건의 무게와 가치를 저장할 리스트

for i in range(n): # 무게와 가치 입력
    a,b = map(int, input().split(" "))
    cost_val.append((a,b))
# print(cost_val[1][1])

for i in range(1,n+1): # 0번은 다 0이므로 1부터 시작
    for j in range(1,k+1):
        w = cost_val[i][0]  # 현재 선택된 물건의 무게
        v = cost_val[i][1] # 현재 선택된 물건의 가치

        if j < w: # 중량제한(j)가 현재 물건의 무게보다 작을때(현재 물건은 못들어감)
            bag[i][j] = bag[i-1][j] # 하나위의 거 그대로 가져옴
        else: # 중량제한이 더 크면
            bag[i][j] = max(v+bag[i-1][j-w], bag[i-1][j]) # max(현재가치+(제한-현재무게)의 무게에서 넣을수 있는값, 하나위의거)


print(bag[n][k]) # 최종적으로 마지막에 최대값이 나옴

