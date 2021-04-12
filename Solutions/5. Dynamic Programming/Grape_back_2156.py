
n = int(input())
grape = []
for i in range(n):
    grape.append(int(input()))

count = [0]*(n+1) # 지나온 과정의 최대값 저장 리스트

count[0] = grape[0] # 예외 처리
if n >=2:
    count[1] = grape[0]+grape[1]

for i in range(2,n): # 2 인덱스부터 시작
    count[i] = count[i-1] # 해당 인덱스의 상태가 0일때로 일단 초기화

    if count[i] < count[i-2]+grape[i]: # 해당 인덱스를 1로 하는게 더 클때
        count[i] = count[i-2]+grape[i] # 두개 이전거에 지금 인덱스값을 더해줌

    if count[i] < count[i-3]+grape[i-1]+grape[i]: #해당 인덱스를 2로 하는게 더 클때
        count[i] = count[i - 3] + grape[i - 1] + grape[i] # 3개전 최대값에 1개전,지금 인덱스값 더해줌줌

print(count[n-1])


# 점화식으로 구할 수도 있음 #현재값 선택안한것이 더 클수도 있는 경우 고려해야함
# for i in range(2,n):
#     count[i] = max(count[i-2]+grape[i],count[i-3]+grape[i-1]+grape[i],count[i-1])
#
# # print(count)
# print(max(count))