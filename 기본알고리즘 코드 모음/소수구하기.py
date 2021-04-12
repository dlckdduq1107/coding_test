import math
import sys
input = sys.stdin.readline

start,end = map(int, input().split(" "))
array = [True for i in range(end+1)] # 끝점까지 구하기 위해

array[1] = False # 1은 소수가 아님
for i in range(2,int(math.sqrt(end))+1): # 2부터 제곱근까지 소수여부에 대해 기록
    if array[i] == True: # 소수이면 그 소수의 배수는 소수가 아님(2배수,3배수...)
        j = 2 # 2를 곱하기 위함
        while i*j <= end: # 소수의 배수가 범위안에 있으면
            array[i*j] = False
            j+= 1

for i in range(start,end+1): # 출력
    if array[i]:
        print(i)