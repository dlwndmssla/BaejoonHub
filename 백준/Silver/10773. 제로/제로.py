n = int(input())
nums = []
for i in range(n):
    m = int(input())
    if m:
        nums.append(m)
    else:
        nums = nums[:-1]
        
print(sum(nums))