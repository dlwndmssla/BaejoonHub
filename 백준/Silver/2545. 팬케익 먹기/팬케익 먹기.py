import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    x = input().split()
    a,b,c,d= map(int, input().split())
    if d!=0:
        for j in range(d):
            k = max(a,b,c)
            if k ==a:
                a -=1
            elif k ==b:
                b -=1
            else:
                c -=1
    print(a*b*c)