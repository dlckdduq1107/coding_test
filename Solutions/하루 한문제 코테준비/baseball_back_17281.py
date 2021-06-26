def dfs(cnt):
    global result # 최종 결과
    if cnt == 9: # 9이면 모든 타순리스트가 다 채워졌을 때임
        pivot, score = 0,0 # 현재 타석순서, 임시 점수
        for ining in a: # 이닝수만큼 반복
            out,b1,b2,b3 = 0,0,0,0 # 아웃카운트, 베이스 1,2,3
            while out < 3: # 아웃카운트가 3미만일 동안
                p = order[pivot] # 현재 피벗에 대한 타석 순서
                value = ining[p] # 타석순서에 따른 예상 안타

                if value == 0: # 아웃일때
                    out += 1 # 카운트 플러스
                elif value ==1: # 1루타 일때
                    score += b3 # 3루의 상태를 더해줌
                    b1,b2,b3 = 1,b1,b2 # 한칸씩 밀어줌
                elif value == 2: # 2루타 일때
                    score += b3+b2 # 2,3루의 상태를 더해줌
                    b1, b2, b3 = 0, 1, b1 # # 두칸씩 밀어줌
                elif value == 3: # 3루타 일때
                    score += b3+b2+b1 # 1,2,3루의 상태를 더해줌
                    b1, b2, b3 = 0, 0, 1 # 3칸씩 밀어줌
                elif value == 4: # 홈런잉때
                    score += b3+b2+b1+1 # 전체 루의 상태 더해줌
                    b1, b2, b3 = 0,0,0 # 상태 초기화

                pivot += 1 # 다음타석으로
                pivot %= 9 # 9이상이면 처음으로 되돌아감(타순)

        result = max(score,result) # 경우마다 최대 값을 최종결과에 넣음
        return

# 타순이 다 채워지지 않았을때
    for i in range(9): # 각 타순마다(1,2,3,4,5,6,7,8,9) 9번씩 반복 -> 최종적으로 하나의 숫자가 모든 자리에 한번씩 들어감
        if dup[i]: # 이미 들어가 있는 위치라면 넘어간다.
            continue
        order[i] = cnt # 해당 인덱스에 타순을 넣어준다.
        dup[i] = 1 # 넣은 후이므로 중복검사에 1을 넣어준다.

        dfs(cnt+1) # dfs실행

        order[i] = 0 # 다시 이전 상태로 되돌리기
        dup[i] = 0

n = int(input()) # 이닝수 입력
a = []
result = 0 # 최대 점수
order = [0 for i in range(9)] # 타순 리스트
dup = [0 for i in range(9)] # 중복 검사를 위한 리스트
order, dup[3] = 0,1 # 첫번째 선수가 4번타자로 정해졌으므로
for i in range(n): # 예상 안타 입력
    a.append(list(map(int,input().split(" "))))

dfs(1) # 백트래킹 실행, 브루트포스
print(result)



