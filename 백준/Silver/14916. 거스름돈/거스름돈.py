import sys,math
input = sys.stdin.readline
a = int(input())
ex1 = []
for i in range(int(a/5),-1,-1):
    b = i*5
    c = (a-b)/2
    if int(c) == float(c):
        ex1.append(i+c)
    
if len(ex1) > 0:
    print(int(min(ex1)))
else:
    print(-1)