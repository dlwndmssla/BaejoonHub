import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    a = int(input())
    k = 0
    for i in range(a):
        c1,c2,r = map(int, input().split())
        if pow(x1-c1,2) + pow(y1-c2,2) < pow(r,2):
            initial = 1
        else:
            initial = 0
        
        if pow(x2-c1,2) + pow(y2-c2,2) < pow(r,2):
            final = 1
        else: 
            final = 0 
        k += abs(initial-final)
    print(k)