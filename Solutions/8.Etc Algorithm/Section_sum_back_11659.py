import sys
input = sys.stdin.readline
n,m = map(int,input().split(" "))
number = list(map(int, input().split(" ")))
sum_value = 0
prefix = [0]
for i in number: # 구간별 합 미리 구하기
    sum_value += i
    prefix.append(sum_value)

for i in range(m):
    a,b = map(int, input().split(" "))
    print(prefix[b]-prefix[a-1])