def check(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)):
            for q in range(j+1,len(nums)):
                temp = nums[i]+nums[j]+nums[q]
                if(check(temp)):
                    answer += 1

    return answer