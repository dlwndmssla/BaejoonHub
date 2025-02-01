import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
trade = [list(map(int,input().split())) for i in range(m)]
# print(trade)
nums = [i for i in range(1+n)]
# print(nums)
for s,e in trade:
    # print(s,e)
    nums[s:e+1] = nums[s:e+1][::-1]
    # print(nums)
print(*nums[1:])