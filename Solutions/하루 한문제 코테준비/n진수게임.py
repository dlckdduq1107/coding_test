def convert(num, base ):
    T = "0123456789ABCDEF"
    q, r = divmod(num, base)

    return convert(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    result = ''
    num = '0'
    for i in range(t*m):
        num += str(convert(i,n))
    print(num)
    j = 0
    next = p
    while(j<t):
        result += num[next]
        next += m
        j+=1

    

    return result
print(solution(2,4,2,1))
print(solution(16,16,2,1))