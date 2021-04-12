import copy
def divide(matrix,m):
    global white, blue  # 개수를 세기 위한 글로벌 변수
    total = 0 # 입력 받은 행렬의 모든 요소 합을 구하기위한 변수
    for i in matrix: # 입력 받은 행렬 모두 탐색
        total += sum(i) # 모든 요소의 합 구함

    if total == 0: # 모든 요소의 합이 0이면 0으로만 이루어져있음
        white += 1 # 하얀색 플러스
    elif total == m*m: # 모든요소의 합이 한변의 길이 제곱이면 모든 요소가 1로만 이루어져 있음
        blue += 1 # 파란색 플러스
    else: # 0과 1이 섞여 있으면
        ##4분할시켜줌###(딥카피 써야 주소도 복사 되지 않음)
        a = copy.deepcopy(matrix[:m//2])
        b = copy.deepcopy(matrix[:m//2])
        c = copy.deepcopy(matrix[m//2:])
        d = copy.deepcopy(matrix[m//2:])
        for j in range(m//2): # 4분할행렬을 만들기 위한 반복
            for q in range(m//2):
                del a[j][m//2]
                del b[j][0]
                del c[j][m//2]
                del d[j][0]

         ### 4분할된 각각의 함수를 길이와 함께 재귀에 넣어줌
        divide(a,m//2)
        divide(b, m // 2)
        divide(c, m // 2)
        divide(d, m // 2)

n = int(input())
white, blue = 0,0
graph = []
for i in range(n): # 입력값을 리스트화 시켜줌
    graph.append(list(map(int, input().split(" "))))

divide(graph,n)
print(white)
print(blue)

