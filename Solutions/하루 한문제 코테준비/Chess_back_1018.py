
n,m = map(int, input().split(" "))

graph = []
for i in range(n):
    graph.append(list(input()))

result = [] #타일을 몇번바꿔야 하는지 기록하는 리스트

for i in range(n-7):
    for j in range(m-7): # 시작점을 가리키는 반복(8X8이므로 시작점을 제한해야함)
        c1 = 0 # 시작을 W로 할때 카운트
        c2 = 0 # 시작을 B로 할때 카운트
        ##시작을 W로 할때와 B로 할때를 나누어서 카운트 해줘야함
        for q in range(i,i+8):
            for w in range(j,j+8): # 8X8모두 탐색
                if (q+w)%2 == 0: # 행과 열을 더해서 2 나머지를 구하면 격자 형태로 if, else가 방문할 수 있다.
                    if graph[q][w] == 'W': # 해당 요소가 W이면 (B로 바꾼다고 가정하고 +1)
                        c2 += 1 # 맨처음이 B로 시작할 때의 카운트
                    if graph[q][w] == 'B': # 해당 요소가 B이면 (W로 바꾼다고 가정하고 +1)
                        c1 += 1# 맨처음이 W로 시작할 때의 카운트
                else:
                    if graph[q][w] == 'B':
                        c2 += 1
                    if graph[q][w] == 'W':
                        c1 += 1
        # 맨처음이 W로 시작할 경우과 B로 시작할 경우에 대한 카운트 추가
        result.append(c1)
        result.append(c2)

print(min(result))