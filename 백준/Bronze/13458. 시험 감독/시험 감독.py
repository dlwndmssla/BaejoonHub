import sys
input = sys.stdin.readline
N = int(input())
ex = list(map(int, input().split()))
b,c = map(int, input().split())
k = 0
for i in range(N):
    if ex[i]<=b:
        k += 1
    else:
        k += 1
        x = ex[i] -b
        if x%c == 0:
            k += x/c
        else:
            k += int(x/c)+1
            
print(int(k))