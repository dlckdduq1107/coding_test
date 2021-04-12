n = int(input())
stair = [0]
for i in range(n): # 입력을 계단으로 리스트화
    stair.append(int(input()))

distance = [0 for i in range(n+1)] # 계단마다 합의 최대값을 저장하는 리스트
if n != 1:  # 길이가 1이 넘을때
    distance[1] = stair[1] # 1번째 세팅
    distance[2] = stair[1]+stair[2] #2번째 세팅

    for i in range(3,n+1): # 3번째 부터 점화식 형식 적용
        distance[i] = max(distance[i-2],distance[i-3]+stair[i-1])+stair[i] # max(두번째 전 최대합,세번째 전 최대합+첫번째 계단값)+현재 계단값
else: # 길이가 1일때 예외처리 해줘야함
    distance[1] = stair[1]
print(distance[n]) # 마지막 계단을 포함한 최대값 출력