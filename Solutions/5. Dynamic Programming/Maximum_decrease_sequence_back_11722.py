n = int(input())
num = list(map(int, input().split(" ")))

distance = [1 for i in range(n)] # 각요소는 그 자체로 길이 1이므로 1로 세팅

for i in range(1,n): # 2번째 부터 탐색
    for j in range(i): # 현재 노드 이전의 노드 모두 탐색
        if num[j] > num[i]: # 현재값보다 이전노드 값이 클때만 길이가 늘어날 수 있음(감소 수열)
            if distance[j]+1 > distance[i]: # 이전노드+1이 현재 값보다 클때 업데이트
                distance[i] = distance[j]+1

print(max(distance))