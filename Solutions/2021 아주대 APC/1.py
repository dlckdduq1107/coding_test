import sys
import math
# input = sys.stdin.readline()

birth = list(map(int,list(input())))
n = int(input())
coding = []
for i in range(n):
    coding.append(list(map(int,list(input()))))

result = []
for each in coding:
    temp = 1
    emp=0
    for i in range(4):
        emp += math.pow(abs(birth[i]-each[i]),2)
    temp *= emp
    emp=0
    for i in range(4,6):
        emp += math.pow(abs(birth[i]-each[i]),2)
    temp *= emp
    emp=0
    for i in range(6,8):
        emp += math.pow(abs(birth[i]-each[i]),2)
    temp *= emp
    result.append([temp,"".join(list(map(str,each)))])

result.sort(key=lambda x:x[1])
result.sort(key=lambda x:x[0],reverse=True)
print(result[0][1])