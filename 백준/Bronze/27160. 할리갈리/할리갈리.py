import sys
input = sys.stdin.readline
a = int(input())
ex1 = ['STRAWBERRY', 'BANANA', 'LIME', 'PLUM']
ex2 = [0]*4
for i in range(a):
    a = list(input().split())
    idx = ex1.index(a[0])
    ex2[idx] += int(a[1])

if 5 in ex2:
    print('YES')
else:
    print('NO')