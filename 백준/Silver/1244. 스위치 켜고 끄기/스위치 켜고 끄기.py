
import sys
input = sys.stdin.readline
n = int(input())
nums = [0]+list(map(int,input().split()))

#남학생1, 여학생2
for _ in range(int(input())):
    g,x = list(map(int,input().split())) #gender, number_x
    if g == 2:
        nums[x] = 1-nums[x]
        for i in range(1,n):
            if (x-i > 0) and (x+i < n+1) and nums[x-i] == nums[x+i]:
                nums[x-i] = 1-nums[x-i]
                nums[x+i] = 1-nums[x+i]
            else: break
            # print(nums)
    else:
        for i in range(1,n//x+1):
            if x*i > n+1: break
            nums[x*i] = 1-nums[x*i]
            # print(nums)
            
nums = nums[1:]
for i in range(n//20+1):
    print(*nums[i*20:(i+1)*20])