def search(start,visited,temp_len): # 재방문하지 않고 갈수 있는 최대의 길이 리턴
    start -=1 # 인덱스가 1부터 이므로
    if(visited[start] == 1): # 방문 했으면
        return temp_len # 길이 리턴
    else: # 방문하지 않았으면
        visited[start] = 1 # 방문 표시
        t = search(graph[start],visited,temp_len+1) # 길이 +1하고 다음 노드로 방문
        return t # 최종 길이 리턴

n = int(input())
graph = []
for i in range(n):
    graph.append(int(input()))

max_len = 0
result = -1
for num,go in enumerate(graph): # 입력된 값 탐색
    visited = [0 for i in range(n)] # 방문 여부 리스트
    temp = search(num+1,visited,0) # 재방문하지 않은 최대의 길이 리턴
    if(max_len<temp): # 길이비교해서 더 크면
        result = num # 인덱스 저장
        max_len = temp # 값 저장
print(result+1)
