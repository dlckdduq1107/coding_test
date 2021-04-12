n = int(input())
graph = []
distance = [1 for i in range(n)] # 가장긴 증가하는 수열 길이 저장을 위한 리스트
stamp_b = [] # b전봇대의 값을 넣기 위한 리스트

for i in range(n): # 입력값 리스트화
    a,b = map(int, input().split(" "))
    graph.append((a,b))

graph.sort() # 첫번째 전봇대 기준으로 정렬

for i,j in graph: # 정렬된 b전봇대의 값을 리스트에 추가
    stamp_b.append(j)

for i in range(n): # 가장 긴 증가하는 수열 찾기
    for j in range(i): # 현재보다 이전노드 모두 탐색
        if stamp_b[i] > stamp_b[j]: # 현재노드가 더 클때만 업데이트 가능
            if distance[i] < distance[j]+1: # 이전노드+1이 현재보다 더 크면 업데이트
                distance[i] = distance[j]+1

print(n-max(distance))