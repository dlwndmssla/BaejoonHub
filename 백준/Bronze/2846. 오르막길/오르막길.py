n = int(input())
nums = list(map(int,input().split()))
nums_sign = [0 for i in range(len(nums))] #모든수를 0으로 시작. 증가하는지 여부(>임 >= 아님)
ans = 0
for i,x in enumerate(nums[1:]): 
    if (x > nums[i]): #이전수가 현재수보다 작고, 이전수가 감소하지 않았다면
        nums_sign[i+1] += nums[i+1]-nums[i]+nums_sign[i] # 이전수와 현재수의 차에 이전까지의 누적값을 더함
        ans = max(ans,nums_sign[i+1])

print(ans)