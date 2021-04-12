n = int(input())
k = int(input())

start,end = 1,n**2 # 이분탐색이용위한 시작,끝

while start <= end: # 이분탐색
    mid = (start+end)//2

    num = 0
    for i in range(1,n+1): # mid가 몇번쨰 숫자인지 구함
        num += min(n,mid//i) # 최대개수는 행개수이고, mid이하의 해당 배수(1~n)의 개수를 모두 더하면 mid가 몇번째인지 나온다.

    if num >= k: # mid의 번호가 k보다 크거나 같으면
        res = mid # 결과저장
        end = mid-1
    else:
        start = mid+1

print(res)