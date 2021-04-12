n = int(input())
a = []
for i in range(n):
    q,w,e,r = input().split(" ")
    w,e,r = int(w),int(e),int(r)
    a.append((q,w,e,r))

a.sort(key=lambda x:x[0])
a.sort(key=lambda x:x[3],reverse=True)
a.sort(key=lambda x:x[2])
a.sort(key=lambda x:x[1],reverse=True)

for i in a:
    print(i[0])