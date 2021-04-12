n = int(input())

num = []

for i in range(n):
    num.append(list(map(int,input().split(" "))))

num.sort(key=lambda x:x[1])
num.sort(key=lambda x:x[0])

for i,j in num:
    print(i,j)

