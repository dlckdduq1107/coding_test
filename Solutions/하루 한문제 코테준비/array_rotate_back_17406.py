import copy

def size_array(temp): # 배열의 최소값 구하는 함수
    s = int(1e9)
    for i in temp:
        s = min(s,sum(i))
    return s

def rotate_array(r,c,s,temp): # 배열 회전시키는 함수
    r -= 1 # 인덱스 맞춰주기위함
    c -= 1

    board = copy.deepcopy(temp) # 입력받은 배열 복사
    for j in range(1,s+1):
        cnt = 2 * j
        tmp = board[r - j][c + j]  # 가장 오른쪽 상위 값

        for k in range(cnt):  # 위 : 왼쪽에서 오른쪽 이동(->)
            board[r - j][c + j - k] = board[r - j][c + j - k - 1]
        for k in range(cnt):  # 왼쪽 : 아래쪽에서 위쪽으로 이동(^)
            board[r - j + k][c - j] = board[r - j + k + 1][c - j]
        for k in range(cnt):  # 아래 : 오른쪽에서 왼쪽으로 이동(<-)
            board[r + j][c - j + k] = board[r + j][c - j + k + 1]
        for k in range(cnt - 1):  # 오른쪽 : 위쪽에서 아래쪽으로 이동(v)
            board[r + j - k][c + j] = board[r + j - k - 1][c + j]

        board[r - j + 1][c + j] = tmp

    return board # 회전한 배열 리턴




def dfs(cnt):
    global result # 최종결과
    if cnt == k: # 인덱스 저장하는 배열 다채워지면
        temp = copy.deepcopy(A) # 배열 카피
        for order in index: # 정해진 순서대로 반복실행
            row,col,size = rotate[order]
            temp = rotate_array(row,col,size,temp) # 배열 회전
        score = size_array(temp) # 사이즈 구하기
        result = min(score,result) # 최소값 구하기
        return

    for i in range(k): # 모든 경우의 수 순서 안 넣은곳에 넣기
        if dup[i]: # 이미 넣었으면
            continue # 패스

        index[i] = cnt # 순서넣기
        dup[i] = 1

        dfs(cnt+1) #dfs실행

        index[i] = 0 # 이전상태로 되돌리기
        dup[i] = 0

n,m,k = map(int,input().split(" "))

A = [] # 배열
rotate = [] # 회전 정보
index = [0 for i in range(k)] # 순서 저장 리스트
dup = [0 for i in range(k)] # 중복 검사 리스트
result = int(1e9) # 최종 결과

for i in range(n):
    A.append(list(map(int,input().split(" "))))
for i in range(k):
    rotate.append(list(map(int, input().split(" "))))


dfs(0)
print(result)