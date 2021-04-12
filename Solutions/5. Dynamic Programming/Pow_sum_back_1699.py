import math

n = int(input())
pow_list = [i for i in range(n+1)]

for i in range(4,n+1): # 4부터 n까지
    for j in range(i): # 현재수보다 작은 제곱수를 찾기위해
        if j**2 <= i: # 제곱수가 현재수 보다 작으면
            if pow_list[i] > pow_list[i-j**2]: # 현재 값이 제곱수를 뺀수보다 크면
                pow_list[i] = pow_list[i-j**2] +1 # 제곱수를 뺀 값 + 하나의 경우의수
        else:
            break
# print((pow_list))
print(pow_list[n])