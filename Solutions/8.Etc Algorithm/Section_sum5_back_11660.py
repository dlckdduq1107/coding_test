import sys
input = sys.stdin.readline
n,m = map(int,input().split(" "))
number = []
for i in range(n):# 입력 리스트화
    number.append(list(map(int, input().split(" "))))
sum_value = 0
prefix = [[0 for j in range(n+1)] for i in range(n)] # 첫번째 행 맨앞은 0, 나머지 행 맨앞은 이전행의 마지막까지 더한값으로 세팅
                                                    # 각 행마다 맨앞에 요소하나가 더 추가된 셈

for i,i_list in enumerate(number): # 구간별 합 미리 구하기
    prefix[i][0] = sum_value # 각행마다 맨앞은 이전행 마지막 합으로 세팅(맨처음은 0으로 세팅)
    for j,value in enumerate(i_list):# 부분합 넣어주기
        sum_value += value
        prefix[i][j+1] = sum_value

# print(number)
for i in range(m): # 입력수만큼 반복
    x1,y1,x2,y2 = map(int, input().split(" "))

    part_sum = 0 # 총합 구하는 변수
    for j in range(x1-1,x2): # 범위내의 행안에서 반복
        part_sum += prefix[j][y2]-prefix[j][y1-1] # 햏마다의 부분합을 더해줌
        # print(part_sum)

    # print(prefix)
    print(part_sum)