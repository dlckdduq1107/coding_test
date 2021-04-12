case = int(input())
for i in range(case):
    n = int(input())
    sequence = [0]*100
    sequence[0] = 1
    sequence[1] = 1
    sequence[2] = 1
    sequence[3] = 2
    sequence[4] = 2

    for j in range(5,n):
        sequence[j] = sequence[j-1]+sequence[j-5]

    print(sequence[n-1])

