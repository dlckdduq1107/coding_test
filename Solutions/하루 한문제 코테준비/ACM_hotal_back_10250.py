import math
t = int(input())
for i in range(t):
    pivot = 0
    result = 0
    h,w,n = map(int, input().split(" "))

    result += math.ceil(n/h) #올림해서 가로를 결정함

     # %를 이용해서 세로(층)을 결정함
    if n%h == 0:
        result+= h*100
    else:
        result += (n%h)*100

    print(result)
