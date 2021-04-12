n,m,k = map(int, input().split())
n_list = [i for i in range(1,n+1)]

if m+k-1 <= n <= m*k:# 조건에 해당할때
    pivot = k # 피벗
    for i in range(1,k+1): # 먼저 최대 길이k개 선택
        print(n_list[pivot - i], end=" ")

    while m != 1: # 1로 나눌때 까지 반복
        n -= k # 전체개수에서 출력한거 빼줌
        m -= 1# 몇개로 나누어야 할지 리프레쉬
        k = n//m # 몇개 선택할지 업데이트
        pivot += k # 리버스 출력위한 피벗 업데이트
        for i in range(1, k + 1): # 리버스 출력
            print(n_list[pivot - i], end=" ")
else:
    print(-1)