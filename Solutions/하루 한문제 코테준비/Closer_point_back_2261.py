import math
n = int(input())
point = []
for i in range(n):
    a,b = map(int, input().split(" "))
    point.append([a,b])

length = int(1e12)
point.sort()

dl = int(1e9)
for i,value_i in enumerate(point[:n//2]):
    x1,y1 =value_i
    for j in range(i+1,n//2):
        x2,y2 = point[j]
        distance = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
        dl = min(dl,distance)

dr = int(1e9)
for i,value_i in enumerate(point[n//2:]):
    x1,y1 =value_i
    ii = n//2 + i
    for j in range(ii+1,n):
        x2,y2 = point[j]
        distance = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
        dr = min(dr,distance)


min_distance = min(dl,dr)

point.sort(key = lambda x:x[1])

for i in range(n):
    x1, y1 = point[i]
    for j in range(i+1,n):
        x2, y2 = point[j]
        dist = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
        if dist > min_distance:
            break
        else:
            min_distance = dist

print("%0.f"%(min_distance**2))

###실패###

