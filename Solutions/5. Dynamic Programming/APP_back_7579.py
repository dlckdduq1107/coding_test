N,M = map(int,input().split(" "))
m_list = [0]+list(map(int,input().split(" ")))
c_list = [0]+list(map(int,input().split(" ")))

bag = [[0 for i in range(sum(c_list)+1)] for j in range(N+1)] # 코스트의 합과 앱의개수에 +1씩한 매트릭스

res = sum(c_list) # 결과값을 최대로 설정
for i in range(1,N+1): # 0번은 다 0이므로 1부터 시작
    for j in range(1,sum(c_list)+1):
        m = m_list[i] # 현재의 메모리
        c = c_list[i] # 현재의 코스트

        if j < c: # 코스트가 현재의 코스트 보다 작으면 선택불가
            bag[i][j] = bag[i-1][j] # 하나위의 거 그대로 가져옴
        else: # 코스트가 현재의 코스트보다 크면 선택가능
            bag[i][j] = max(m+bag[i-1][j-c], bag[i-1][j]) # max(현재메모리+(코스트-현재코스트)의 메모리에서 넣을수 있는값, 하나위의거)

        if bag[i][j] >= M: # 제한 조건 만족하면
            res = min(res,j) # 그중에 가장 작은거 선택


print(res)