def fib(num):
    if num == 1 or num == 2:
        f[num] = num
    if f[num] != 0:
        return f[num]

    f[num] = fib(num-1)+fib(num-2)
    return f[num]

n = int(input())
f = [0]*1001
d = [0]*1001
d[1] = 1
d[2] = 2
for i in range(3,n+1):
    d[i] = d[i-1]+d[i-2]

fib(n)
print(d[n]%10007)
print(fib(n)%10007)