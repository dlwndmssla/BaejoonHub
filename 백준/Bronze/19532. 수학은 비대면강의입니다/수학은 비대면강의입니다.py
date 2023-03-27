import sys
input=sys.stdin.readline
a,b,c,d,e,f = map(int, input().split())

if a!= 0 and d!= 0:
    y = int((c*d-a*f)/(b*d-a*e))
elif a == 0:
    y = int(c/b)
else:
    y = int(f/e) 
    
if a!=0:
    x = int((c-y*b)/a)
else:
    x = int((f-y*e)/d)
    
print(x,y)