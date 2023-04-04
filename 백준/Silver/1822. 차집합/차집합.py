import sys
input = sys.stdin.readline
a,b = map(int, input().split())
ex1 = set(map(int, input().split()))
ex2 = set(map(int, input().split()))
k = 0
ans = set()
for i in ex1:
    if i not in ex2:
        ans.add(i)

if len(ans) != 0:
    print(len(ans))
    print(*sorted(ans))
else:
    print(0)