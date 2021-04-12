n = int(input())
num = list(map(int, input().split(" ")))

pre_num = num[:]
pre_distance = [1 for i in range(n)]

#맨앞에서 부터 가장 긴 증가하는 수열 구하기
for i in range(1,n): # 2번째 부터 탐색
    for j in range(i): # 현재 노드 이전의 노드 모두 탐색
        if pre_num[j] < pre_num[i]: # 현재값보다 이전노드 값이 작을때만 길이가 늘어날 수 있음(증가 수열)
            if pre_distance[j]+1 > pre_distance[i]: # 이전노드+1이 현재 값보다 클때 업데이트
                pre_distance[i] = pre_distance[j]+1


 # 맨뒤에서 부터 가장 긴 증가하는 수열 구하기
post_num = num[:]
post_distance = [1 for i in range(n)]
for i in range(n-1,-1,-1): # 맨 끝에서 부터 맨 앞까지
    for j in range(i+1,n): # 현재 노드 다음의 노드 모두 탐색
        if post_num[j] < post_num[i]: # 현재값보다 다음노드 값이 작을때만 길이가 늘어날 수 있음(증가 수열)
            if post_distance[j]+1 > post_distance[i]: # 이전노드+1이 현재 값보다 클때 업데이트
                post_distance[i] = post_distance[j]+1

result = [0 for i in range(n)]
for i in range(n): # 최종 결과 길이 리스트
    result[i] = pre_distance[i]+post_distance[i]
print(max(result)-1)