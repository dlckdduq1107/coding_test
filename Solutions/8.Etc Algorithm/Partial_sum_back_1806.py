n,s = map(int,input().split(" "))
number = [0]
number += list(map(int, input().split(" ")))
sum_value = 0
prefix = []
for i in number: # 구간별 합 미리 구하기
    sum_value += i
    prefix.append(sum_value)

start,end = 1,1 # number리스트 맨앞에 0이 있어서 1로 설정

result = int(1e9)
while start <= n and end <= n: # 투포인트가 범위를 안벗어날 동안
    res = prefix[end]-prefix[start-1] #투포인터 사이의 합
    if start == end: # 포인터가 같으면 하나의 값임
        res = number[start]
    if res < s: # 합이 더 작으면 end를 한 칸 뒤로
        end += 1
    else: # 합이 더 클때
        if end-start+1 < result: # 길이가 더 작으면 길이 업데이트
            result = end-start+1
        start += 1 # start를 뒤로 한칸
if number[1] >= s or number[n] >= s: # 처음과 끝이 설정값을 넘을 때는 제일 작은게 1이됨
    print(1)
    exit(0)
if result == int(1e9): # 길이가 업데이트 되지 않았을때
    print(0)
else: # 업데이트 되었을때
    print(result)