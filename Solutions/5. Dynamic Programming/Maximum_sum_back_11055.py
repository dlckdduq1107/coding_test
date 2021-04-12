n = int(input())

num = list(map(int, input().split(" ")))
sum_num = num[:] # 합계 구하기 위한 값 리스트 복사

for i in range(1,n): # 2번째 부터 탐색
    for j in range(i): # 현재노드 이전 모든 노드를  탐색
        if num[i] > num[j]: # 현재 노드가 더 크고
            if sum_num[j]+num[i] > sum_num[i]: # 현재 합이 이전 노드+현재값 보다 작을때 업데이트
                sum_num[i] = sum_num[j]+num[i]

print(max(sum_num))




#
# n = int(input())
#
# num = list(map(int, input().split(" ")))
# sum_num = [0 for i in range(n)]#num[:]
#
# for i in range(n):
#     sum_num[i] = num[i]
#     for j in range(i):
#         if num[i] > num[j] and sum_num[j]+num[i] > sum_num[i]:
#             sum_num[i] = sum_num[j]+num[i]
# # print(num)
# # print(sum_num)
# print(max(sum_num))