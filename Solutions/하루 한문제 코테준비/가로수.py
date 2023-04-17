def division(gnum, snum):
    while snum != 0:
        gnum, snum = snum, gnum%snum
    return gnum
    

n = int(input())
nums = [] 
for i in range(n):
    nums.append(int(input()))
nums.sort()
start, end = nums[0], nums[-1]

differs = []
for i in range(len(nums)-1):
    differs.append(abs(nums[i]-nums[i+1]))


gcd = differs[-1]
for i in differs:
    gcd = division(gcd, i)
# print(gcd)

result = 0
for i in differs:
    result += i//gcd -1

print(result)
