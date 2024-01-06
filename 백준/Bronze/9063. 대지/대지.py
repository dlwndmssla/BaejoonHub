n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    if i == 0:
        x0,x1,y0,y1 = a,a,b,b
    x0 = min(x0,a)
    x1 = max(x1,a)
    y0 = min(y0,b)
    y1 = max(y1,b)
    
print((x1-x0)*(y1-y0))