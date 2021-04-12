def fib(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    if f[x] != 0:
        return f[x]
    f[x] = fib(x-1)+fib(x-2)
    return f[x]
##이전꺼에 +0한경우와 2개전꺼에 +01한 경우를 합치면 다음경우가 나온다.##

n = int(input())
f = [0]*(n+1)
print(fib(n-1))

