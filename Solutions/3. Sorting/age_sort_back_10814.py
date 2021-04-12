n = int(input())
a = []
for i in range(n):
    q,w = input().split(" ")
    q = int(q)
    a.append((q,w,i))

a.sort(key=lambda x:x[2])
a.sort(key=lambda x:x[0])


for i,j,q in a:
    print(i,j)