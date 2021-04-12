import math
import sys
input = sys.stdin.readline
n = int(input())

##소수구하기 부분##
array = [True for i in range(n+1)] # 소수판별하는 리스트

array[1] = False # 1은 소수가 아님
for i in range(2,int(math.sqrt(n))+1): # 2부터 제곱근까지 소수여부에 대해 기록
    if array[i] == True: # 소수이면 그 소수의 배수는 소수가 아님(2배수,3배수...)
        j = 2 # 2를 곱하기 위함
        while i*j <= n: # 소수의 배수가 범위안에 있으면
            array[i*j] = False
            j+= 1

##부분합 구하기 부분###
decimal_list = [[0,0]] # [소수,부분합]
sum_value = 0 # 부분합 넣어주기 위한 변수
for i in range(1,n+1): # 입력된 숫자까지 반복
    if array[i] == True: # 소수이면
        sum_value += i
        decimal_list.append([i,sum_value]) # 소수와 현재까지의 부분합 추가


# for q,(i,j) in enumerate(decimal_list):
#     sum_value += i
#     decimal_list[q][1] = sum_value


##투포인터 부분###(start,end를 같이 시작해서 탐색)
start,end = 1,1 # 둘다 맨처음으로 세팅
count = 0 # 개수 카운트 변수
while start != len(decimal_list) and end != len(decimal_list): # start와 end가 끝까지 갈때까지 반복(하나라도 번위 넘어가면 빠져나옴)
    deci_sum = decimal_list[end][1] - decimal_list[start-1][1] # start부터 end까지의 연속된 소수 부분합

    if deci_sum == n: # 연속된 소수 부분합이 찾는 값이면 개수 카운트
        count += 1
        # print(start,end)

    if deci_sum < n: # 부분합이 찾는값보다 작으면 end를 한칸 뒤로
        end += 1
    else: # 부분합이 찾는 값보다 크면 start를 한칸 뒤로
        start += 1



# print(decimal_list)
print(count)