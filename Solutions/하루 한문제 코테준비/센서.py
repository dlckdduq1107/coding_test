n = int(input())
count = int(input())
sensors = list(map(int,input().split(" ")))

sensors.sort()

differ = []
for i in range(n):
    if i+1<n:
        differ.append(sensors[i+1]-sensors[i])
differ.sort(reverse=True)
for i in range(count-1):
    if(differ !=[]):
        differ.pop(0)
print(sum(differ) if differ != [] else 0)