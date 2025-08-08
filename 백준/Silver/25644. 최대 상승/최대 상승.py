n = int(input())
nums = list(map(int,input().split()))

min0,max0 = float('inf'),-float('inf')
for i in nums:
    min0 = min(min0,i)
    max0 = max(max0,i-min0)
print(max0)