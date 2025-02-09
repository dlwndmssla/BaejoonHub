n = int(input())
nums = list(map(int,input().split()))
nums_sign = [0 for i in range(len(nums))]
ans = 0
for i,x in enumerate(nums[1:]):
    if (x > nums[i]) and (nums_sign[i] >= 0):
        nums_sign[i+1] += nums[i+1]-nums[i]+nums_sign[i]
        ans = max(ans,nums_sign[i+1])

print(ans)