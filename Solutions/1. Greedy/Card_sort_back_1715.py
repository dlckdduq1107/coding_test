import heapq
n = int(input())
card = []

for i in range(n):
    heapq.heappush(card,int(input())) #우선 순위큐 푸쉬

res = 0
while len(card) > 1: # 두개이상 남았을 경우만 pop이 가능
    a = heapq.heappop(card) # 가장 작은 두수 pop
    b = heapq.heappop(card)
    # print(a,b)
    addition = a+b
    res += addition # 최종결과에 두수 합한거 더하기
    heapq.heappush(card,addition) # 우선순위큐에 두수 더한거 추가

if n == 1:
    print(0)
else:
    print(res)