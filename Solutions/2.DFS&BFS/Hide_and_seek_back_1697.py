from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start) # 시작구간 설정

    while queue:
        v = queue.popleft()

        if v == k: # 목표지점에 도달했을때 빠져나오기
            break
        search_list = [v-1,v+1,v*2] # 세가지의 경우를 BFS
        for i in search_list:
            if i < 0 or i > k*2: # 범위를 2배로 잡고 안에 있는 경우만 탐색
                continue
            if matrix[i] <= matrix[v]+1 and matrix[i] != 0: # 0 아니면 처음아니므로 패스, 업데이트 할 수가 더 크면 가장 빠른 길이 아니므로 패스
                # queue.append(i) # 업데이트 안된 길은 큐에 추가할 필요 없음
                continue
            matrix[i] = matrix[v]+1 # 이전 길에 +1
            queue.append(i)

n,k = map(int,input().split(" "))
matrix = [0]*200002

bfs(n)
if n>k: # 출발지점이 더 멀리있는 경우에는 -1로 돌아오는길 밖에 없음
    print(n-k)
else:
    print(matrix[k])
