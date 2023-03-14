import sys
input = sys.stdin.readline
a,b = map(int, input().split())
ex1 = []
ex2 = []
for i in range(b):
    c,d = map(int, input().split())
    
    if c > 6*d:
        c = 6*d
    
    ex1.append(c)
    ex2.append(d)
    
e = min(int(a/6)*min(ex1) + (a%6)*min(ex2),(int(a/6)+1)*min(ex1) )    
print(e)