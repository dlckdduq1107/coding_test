import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

# rooms = [0 for i in range(n)]
walls = [1 for i in range(n+1)]
result = n+1
for i in range(m):
    x,y = map(int, input().split(" "))
    x,y = x-1, y-1

    for j in range(x+1, y+1): # 벽허물기
        if walls[j] == 0:
            continue
        walls[j] = 0
        result -= 1

print(result-1) # 남아있는 방개수 출력