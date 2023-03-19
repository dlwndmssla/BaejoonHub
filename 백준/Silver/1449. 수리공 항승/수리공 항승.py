import sys,math
input = sys.stdin.readline
a,b = map(int, input().split())
ex1 = list(map(int, input().split()))
ex2 = [1]*a
ex1.sort()
for i in range(a-1):
    for j in range(i+1,a):
        if ex1[i] + b -1 < ex1[j]:
            break
        elif ex2[i] == 0:
            break
        else:
            ex2[j] = 0
print(sum(ex2))