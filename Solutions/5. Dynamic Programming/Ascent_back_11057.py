n = int(input())

# 처음은 1로 이후에는 0으로 초기화된 리스트
f = [[1 for i in range(10)]]
for i in range(n-1):
    f.append([0 for i in range(10)])

for i in range(n-1): # 다음꺼를 정해주므로 입력보다 하나줄여서 반복
    for j in range(10): # i,j는 다음요소를 가리키는 용도로 사용
        for q in range(10): # q는 현재 위치보다 작은 j인덱스에서 받아오기 위한 반복
            if q <= j: # 오르막이므로 작은데서 받아와야함
                f[i+1][j] += f[i][q]

print(sum(f[n-1])%10007)