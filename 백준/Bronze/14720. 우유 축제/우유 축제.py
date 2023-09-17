import sys
input=sys.stdin.readline

n = int(input())
ex = list(map(int, input().split()))
x = 0
ans = 0
for i in range(n):
    if ex[i] == x:
        if x == 2:
            x = 0
        else:
            x += 1
        ans += 1
print(ans)