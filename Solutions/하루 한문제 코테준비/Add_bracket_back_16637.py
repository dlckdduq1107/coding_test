from math import inf
from sys import stdin


def dfs(idx, sub_total):
    global answer

    if idx == len(op): # 길이 같으면 계산 다한것임
        answer = max(answer, int(sub_total)) # 최댓값 선택
        return

    #  (3 + 8) * 7 - 9 * 2 부터 시작, 순서대로 계산 하는 것
    first = str(eval(sub_total + op[idx] + nums[idx + 1]))
    dfs(idx + 1, first)

    if idx + 1 < len(op):
        # 3 + (8 * 7) - 9 * 2 부터 시작, 한개뒤에 괄호 쳐서 계산 하는것
        second = str(eval(nums[idx + 1] + op[idx + 1] + nums[idx + 2]))
        second = str(eval(sub_total + op[idx] + second))
        # op를 2개 소모했으므로 idx + 2
        dfs(idx + 2, second)


if __name__ == '__main__':
    n = int(stdin.readline())
    expression = stdin.readline().rstrip()
    nums, op = [], []
    answer = -inf

    for e in expression:
        nums.append(e) if e.isdigit() else op.append(e)

    dfs(0, nums[0])
    print(answer)













#     part_max = -int(1e9)
#     temp = 0
#     buho = '+'
#     for p_p in part:
#         if p_p.isalnum():
#             p_p = int(p_p)
#
#             if buho == "-":
#                 result.append(p_p)
#                 part_max = -int(1e9)
#                 temp = 0
#                 continue
#
#             temp = cal(temp, p_p, buho)
#             if part_max < temp:
#                 part_max = temp
#
#         else:
#             buho = p_p
#             if buho == "-":
#                 if part_max != -int(1e9):
#                     result.append(part_max)
#                 result.append(buho)
#     if buho == '+':
#         result.append(buho)
#         result.append(part_max)
#     result.append("*")
#
# print(result)