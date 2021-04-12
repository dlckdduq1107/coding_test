def fib(x):
    #초기세팅
    if x == 1:
        f[x] = 1
    if x == 2:
        f[x] = 2
    if x == 3:
        f[x] = 4
    if f[x] != 0:# 이미 계산했을때
        return f[x]

    f[x] = fib(x-1)+fib(x-2)+fib(x-3)
    return f[x]

case = int(input())
res = []
for i in range(case):
    n = int(input())
    f = [0]*100
    res.append(fib(n))

for i in res:
    print(i)
