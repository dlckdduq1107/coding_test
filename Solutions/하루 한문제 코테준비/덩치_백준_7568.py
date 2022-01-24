n = int(input())
data = []

for i in range(n):
    data.append(list(map(int,input().split(" "))))

result = [0 for i in range(n)]
for idx,(w,h) in enumerate(data):
    rank = 1
    for j in range(n):
        if(w<data[j][0] and h<data[j][1]):
            rank += 1

    result[idx] = rank

for i in result:
    print(i, end=' ')