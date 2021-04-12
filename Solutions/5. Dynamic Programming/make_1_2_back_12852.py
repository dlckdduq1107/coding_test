n = int(input())

distance = [[0,0] for i in range(n+1)] # [최소거리,어디서 왔는지]의 리스트

for i in range(2,n+1): # 1은 자기자신이므로 0, 2부터 시작
    distance[i][0] = distance[i-1][0] + 1 # 이전꺼에서 왔다고 초기 설정
    distance[i][1] = i-1 # 이전노드 기록

    if i % 2 == 0: # 2로 나누어떨어지고
        if distance[i//2][0]+1 > distance[i][0]: # //2에서 온것이 더 크면 패스
            pass
        else:# //2에서 온것이 더 작으면
            distance[i][0] = distance[i//2][0] +1 # /2노드에서 +1
            distance[i][1] = i//2 # /2노드를 기록(어디서 왔는지)

    if i% 3 == 0:# 3으로 나누어떨어지고
        if distance[i//3][0]+1 > distance[i][0]:# //3에서 온것이 더 크면 패스
            pass
        else:# //3에서 온것이 더 작으면
            distance[i][0] = distance[i//3][0] +1# /3노드에서 +1
            distance[i][1] = i//3# /3노드를 기록(어디서 왔는지)


print(distance[n][0]) # 최소 거리 출력
pivot = n # 왔던길출력하기 위한 피벗
print(n,end=" ") # 출력을 맞춰주기위한 n출력
while pivot != 1: # 1이 될때까지 반복
    print(distance[pivot][1], end=" ") # 자신이 어디서 왔는지 출력
    pivot = distance[pivot][1] # 피벗을 이전노드로 업데이트

