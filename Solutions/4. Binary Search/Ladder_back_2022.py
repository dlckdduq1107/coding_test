import math

x,y,c = map(float,input().split(" "))

start,end = 1, min(x,y) # x,y중 작은 값보다는 거리가 짧다.
d = 0.0 # 최종 결과 거리
while abs(start-end) >= 1e-6: # 오차범위보다 큰 동안 반복 - 실수이기 때문
    mid = (start+end)/2.0

    h1 = math.sqrt(x**2-mid**2)# h1에 대한 정리
    h2 = math.sqrt(y**2-mid**2) # h2에 대한 정리
    h = (h1*h2)/(h1+h2) # 계산 결과 h에 대한 수식

    if c <= h: # 목표값이 더작으면 d가 더 커야함
        d = mid
        start = mid
    else: # 목표값이 더 크면 d를 줄여야함
        end = mid

print("%.3f"%d)

