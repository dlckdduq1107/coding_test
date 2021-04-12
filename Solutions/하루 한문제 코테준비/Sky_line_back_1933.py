import sys
input = sys.stdin.readline
case = int(input())
building = {}
for i in range(case):
    x,h,y = map(int, input().split(" "))
    for j in range(x,y+1):
        if j in building:
            if building[j] < h:
                building[j] = h
        else:
            building[j] = h



pivot = 0
for i in range(max(building.keys())+2):
    if i not in building:
        building[i] = 0
building = dict(sorted(building.items(), key=lambda x:x[0]))

for i,j in enumerate(building):
    if pivot < building[j]:
        print(j,building[j], end=" ")
        pivot = building[j]
    elif pivot > building[j]:
        print(j-1, building[j], end=" ")
        pivot = building[j]
####실패####
