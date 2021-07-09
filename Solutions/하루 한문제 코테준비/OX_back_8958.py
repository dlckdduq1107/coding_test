n = int(input())
for i in range(n):
    score = 0
    a = list(input())
    plus = 1
    for j in a:
        if j == "O":
            score += plus
            plus += 1
        else:
            plus = 1

    print(score)
