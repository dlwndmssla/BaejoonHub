nums = []
for _ in range(int(input())):
    n = int(input())
    if not n: nums.pop()
    else: nums.append(n)
    
print(sum(nums))