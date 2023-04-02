import sys, math
input = sys.stdin.readline
a,b,c,d,e = map(int, input().split())
while [a,b,c,d,e] != [1,2,3,4,5]:
    if a>b:
        a,b = b,a
        print(*[a,b,c,d,e])
    if b>c:
        b,c = c,b
        print(*[a,b,c,d,e])
    if c>d:
        c,d = d,c
        print(*[a,b,c,d,e])
    if d>e:
        d,e = e,d
        print(*[a,b,c,d,e])