import sys
input=sys.stdin.readline
a,b = map(int, input().split())
ex1 = list(map(int, input().split()))
ex2 = [0]
k = 0
for i in range(a):
    k += ex1[i]
    ex2.append(k)

for j in range(b):
    m,n = map(int, input().split())
    print(ex2[n] - ex2[m-1])