n = int(input())
num = [0 for i in range(n+1)]	
path = [[] for i in range(n+1)]	
for i in range(2, n + 1):
    num[i] = num[i - 1] + 1
    path[i] = path[i -1] + [i]
    if i % 3 == 0:
        a = num[i // 3] + 1
        num[i] = min(num[i], a)
        if num[i] == a:
            path[i] = path[i // 3] + [i]
    if i % 2 == 0:
        a = num[i // 2] + 1
        num[i] = min(num[i], a)
        if num[i] == a:
            path[i] = path[i // 2] + [i]
print(num[-1])
ans = path[-1][::-1] + [1]
print(*ans)