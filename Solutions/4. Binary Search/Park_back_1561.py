def check_num(time): # 시간에 따라 끝 번호 어린이가 몇인지 리턴
    num = m
    for i in time_list:
        num += time//i
    return num

n,m = map(int,input().split(" "))

time_list = list(map(int, input().split(" ")))

if n<=m: # 예외처리
    print(n)
    exit(0)


start,end = 0, 2000000000*10000
result = 0
order = 0

while start<= end: # 이분 탐색
    mid = (start+end)//2

    if check_num(mid-1)<n: # 최대 명수를 구하는 거니까 이전꺼의 최대부터 시작해야함
        order = check_num(mid-1) # 최대 명수 저장
        result = mid # 기준 시간 저장
        start = mid+1
    else:
        end = mid-1


for i in range(m): # 기준시간에서 몇번째 기구에 속하는지 구하기
    if result % time_list[i] == 0:
        order += 1
        if n == order:
            print(i+1)
            break

