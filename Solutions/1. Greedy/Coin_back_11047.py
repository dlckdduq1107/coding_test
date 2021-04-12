n, k = map(int, input().split())
have_coin = []
for i in range(n):# input
    have_coin.append(int(input()))

have_coin.reverse()

count = 0
for money in have_coin:
    if(money <= k): # 동전이 남은 금액보다 작으면
        count += k//money #배수만큼 ++
        k -= (k//money)*money # k값 재설정
    if(k == 0): # 조건완료시
        break
print(count)