def fib(n):
    global num1
    if(n==1 or n==2):
        num1 += 1
        return 1
    else: return(fib(n-1)+fib(n-2))
def dpfib(n):
    global num2
    arr = [1 for i in range(n)]
    for i in range(2,n):
        arr[i] = arr[i-1]+arr[i-2]
        num2 += 1
    return arr[n-1]

num1, num2 = 0,0
n = int(input())
fib(n)
dpfib(n)
print(num1, num2)
