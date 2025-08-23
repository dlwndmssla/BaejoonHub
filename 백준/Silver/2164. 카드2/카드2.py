from collections import deque
nums = deque([i for i in range(int(input()))])
while True:
    if len(nums) == 1: break
    nums.popleft()
    a = nums.popleft()
    nums.append(a)
print(nums[0]+1)