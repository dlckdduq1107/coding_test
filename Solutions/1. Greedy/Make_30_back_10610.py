num = list(input())
num = list(map(int, num))

num.sort(reverse=True)

if (sum(num)%3 != 0) or (not (0 in num)):
    print(-1)
else:
    for i in num:
        print(i,end="")

