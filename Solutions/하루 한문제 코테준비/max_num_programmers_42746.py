
def solution(numbers):
    answer = ''

    a = []
    for i in numbers:
        b = str(i)

        a.append([b*3,i])

    a.sort(key=lambda x:x[0], reverse=True)
    # print(a)
    for i,j in a:
        answer += str(j)
    return str(int(answer))


print(solution([3, 30, 34, 5, 9]))