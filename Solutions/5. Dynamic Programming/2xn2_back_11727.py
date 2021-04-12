def fib(x):
    if x == 1: # 초기값세팅
        f[x] = 1
    if x == 2: # 초기값세팅
        f[x] = 3
    if f[x] != 0: # 한번계산했던 결과이면 있는 값 리턴
        return f[x]

    f[x] = fib(x-1)+(fib(x-2)*2)# 식에 대한 점화식
    return f[x] # 계산 하지 않았던 값일때 리턴

f = [0]*1001 # 다이내믹을 위한 리스트
n = int(input())

print(fib(n)%10007)