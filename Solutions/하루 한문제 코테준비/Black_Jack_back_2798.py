n,m = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums.sort()
differ = int(1e9)

for i in range(n-2): # 첫번째 부터 n-2까지
    for j in range(i+1,n-1):
        for q in range(j+1,n): # 숫자 3개 선택하는 모든 경우의수
            limit = m - (nums[i] + nums[j] + nums[q]) # 임계값과의 차이
            if limit >= 0: # 차이가 0보다 클때만 판단
                if differ > limit: # 이전차이보다 더 작을때
                    differ = limit # 업데이트
                    result = nums[i]+nums[j]+nums[q]
            else:
                continue

print(result)