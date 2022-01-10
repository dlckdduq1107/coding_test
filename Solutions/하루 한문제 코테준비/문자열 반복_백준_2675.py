n = int(input())

for i in range(n):
    result = ''
    R,S = input().split(" ")
    R = int(R)
    for j in S:
        result += R*j
    print(result)


