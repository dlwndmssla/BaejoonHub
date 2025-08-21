from collections import deque
nums = deque([i for i in range(1,1+int(input()))])
deleted = deque([])
while True:
    if len(nums) == 1: break
    deleted.append(nums.popleft())
    a = nums.popleft()
    nums.append(a)
print(*(deleted+nums))